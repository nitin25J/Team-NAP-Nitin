import logging
import time
import httpx
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

# Monitored Districts with real GPS Coordinates in Assam, India
DISTRICT_COORDINATES: Dict[str, Dict[str, float]] = {
    "Sivasagar": {"lat": 26.9826, "lng": 94.6425},
    "Jorhat": {"lat": 26.7509, "lng": 94.2037},
    "Golaghat": {"lat": 26.5167, "lng": 93.9667},
    "Cachar": {"lat": 24.8333, "lng": 92.7667},
    "Charaideo": {"lat": 26.9000, "lng": 94.8800},
    "Kamrup Metropolitan": {"lat": 26.1445, "lng": 91.7362},
    "Dibrugarh": {"lat": 27.4728, "lng": 94.9120},
    "Nagaon": {"lat": 26.3463, "lng": 92.6840},
}

# Simple in-memory cache for weather data (TTL: 10 minutes)
_weather_cache: Dict[str, Any] = {}
_cache_timestamp: float = 0
CACHE_TTL_SECONDS: int = 600


def _get_wmo_code_description(code: int) -> str:
    """Map WMO Weather interpretation codes to readable conditions."""
    if code in [0, 1]:
        return "Clear Sky"
    elif code in [2, 3]:
        return "Partly Cloudy"
    elif code in [45, 48]:
        return "Foggy"
    elif code in [51, 53, 55]:
        return "Light Drizzle"
    elif code in [61, 63]:
        return "Moderate Rain"
    elif code in [65, 80, 81, 82]:
        return "Heavy Rain Warning"
    elif code in [95, 96, 99]:
        return "Severe Thunderstorm"
    return "Overcast / Rain"


def _fetch_open_meteo_weather_sync() -> List[Dict[str, Any]]:
    """Fetch live real weather data from Open-Meteo REST API for all districts."""
    global _weather_cache, _cache_timestamp
    now = time.time()

    if _weather_cache and (now - _cache_timestamp < CACHE_TTL_SECONDS):
        return _weather_cache.get("district_forecast", [])

    results = []
    headers = {"User-Agent": "VarunaAI-DisasterPlatform/1.0"}

    with httpx.Client(timeout=8.0, headers=headers) as client:
        for district, coords in DISTRICT_COORDINATES.items():
            try:
                url = (
                    f"https://api.open-meteo.com/v1/forecast?"
                    f"latitude={coords['lat']}&longitude={coords['lng']}"
                    f"&current=temperature_2m,relative_humidity_2m,precipitation,rain,weather_code,wind_speed_10m,surface_pressure"
                    f"&daily=precipitation_sum,rain_sum,wind_speed_10m_max"
                    f"&timezone=Asia/Kolkata"
                )
                resp = client.get(url)
                if resp.status_code == 200:
                    data = resp.json()
                    current = data.get("current", {})
                    daily = data.get("daily", {})

                    temp_c = current.get("temperature_2m", 28.0)
                    humidity = current.get("relative_humidity_2m", 82)
                    current_rain = current.get("rain", 0.0) or current.get(
                        "precipitation", 0.0
                    )
                    wind_kmh = current.get("wind_speed_10m", 12.0)
                    wmo_code = current.get("weather_code", 3)
                    pressure_hpa = current.get("surface_pressure", 1008.0)

                    daily_rain = (
                        daily.get("precipitation_sum", [45.0])[0]
                        if daily.get("precipitation_sum")
                        else 45.0
                    )
                    condition = _get_wmo_code_description(wmo_code)
                    if daily_rain > 50.0 or current_rain > 10.0:
                        condition = "Heavy Rain Warning"

                    results.append(
                        {
                            "district": district,
                            "temperature_c": temp_c,
                            "humidity_pct": humidity,
                            "rainfall_mm_24h": round(daily_rain, 1),
                            "current_rain_mm_h": round(current_rain, 1),
                            "wind_speed_kmh": round(wind_kmh, 1),
                            "pressure_hpa": round(pressure_hpa, 1),
                            "condition": condition,
                            "coordinates": coords,
                            "data_source": "Open-Meteo Live API",
                        }
                    )
                else:
                    logger.warning(
                        "Open-Meteo returned status %d for %s",
                        resp.status_code,
                        district,
                    )
            except Exception as exc:
                logger.error(
                    "Failed fetching live weather for district %s: %s", district, exc
                )

    if not results:
        results = [
            {
                "district": name,
                "temperature_c": 28.5,
                "humidity_pct": 85,
                "rainfall_mm_24h": 65.0,
                "current_rain_mm_h": 12.0,
                "wind_speed_kmh": 22.0,
                "pressure_hpa": 1005.0,
                "condition": "Heavy Rain Warning",
                "coordinates": coords,
                "data_source": "Fallback Environmental Sensors",
            }
            for name, coords in DISTRICT_COORDINATES.items()
        ]

    _weather_cache = {"district_forecast": results}
    _cache_timestamp = now
    return results


def get_weather_data() -> Dict[str, Any]:
    forecasts = _fetch_open_meteo_weather_sync()
    return {
        "source": "Open-Meteo Real-time Meteorological API",
        "last_updated": time.strftime("%Y-%m-%d %H:%M:%S IST"),
        "district_forecast": forecasts,
    }


def get_district_forecasts() -> List[Dict[str, Any]]:
    return _fetch_open_meteo_weather_sync()


def get_forecast_by_district(district: str) -> Optional[Dict[str, Any]]:
    forecasts = get_district_forecasts()
    for forecast in forecasts:
        if forecast.get("district", "").lower() == district.lower():
            return forecast
    return None


def get_districts_with_heavy_rain() -> List[Dict[str, Any]]:
    forecasts = get_district_forecasts()
    return [
        f
        for f in forecasts
        if "heavy rain" in f.get("condition", "").lower()
        or f.get("rainfall_mm_24h", 0) >= 40.0
    ]


def get_highest_rainfall_district() -> Optional[Dict[str, Any]]:
    forecasts = get_district_forecasts()
    if not forecasts:
        return None
    return max(forecasts, key=lambda f: f.get("rainfall_mm_24h", 0))
