import logging
from typing import Any, Dict, List, Optional

from app.database.loader import load_json

logger = logging.getLogger(__name__)

FILENAME = "weather.json"


def get_weather_data() -> Dict[str, Any]:
    """Return the full weather forecast dataset."""
    data = load_json(FILENAME)
    if not isinstance(data, dict):
        logger.warning("Weather data malformed or empty")
        return {}
    return data


def get_district_forecasts() -> List[Dict[str, Any]]:
    """Return weather forecasts for all districts."""
    data = get_weather_data()
    return data.get("district_forecast", [])


def get_forecast_by_district(district: str) -> Optional[Dict[str, Any]]:
    """Return the weather forecast for a specific district."""
    forecasts = get_district_forecasts()
    for forecast in forecasts:
        if forecast.get("district", "").lower() == district.lower():
            return forecast
    logger.warning("Forecast not found for district: %s", district)
    return None


def get_districts_with_heavy_rain() -> List[Dict[str, Any]]:
    """Return districts currently forecast with heavy or very heavy rain."""
    forecasts = get_district_forecasts()
    return [
        f for f in forecasts
        if "heavy rain" in f.get("condition", "").lower()
    ]


def get_highest_rainfall_district() -> Optional[Dict[str, Any]]:
    """Return the district forecast with the highest 24h rainfall."""
    forecasts = get_district_forecasts()
    if not forecasts:
        return None
    return max(
        forecasts,
        key=lambda f: f.get("rainfall_mm_24h", 0) if isinstance(f.get("rainfall_mm_24h"), (int, float)) else 0
    )