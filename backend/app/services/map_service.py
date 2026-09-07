import logging
from typing import Any, Dict, List
from app.services import prediction_service

logger = logging.getLogger(__name__)

# Default GIS center: Guwahati Command Base
GUWAHATI_CENTER = {"lat": 26.1445, "lng": 91.7362}


def get_map_data() -> Dict[str, Any]:
    """Return GIS disaster map dataset constructed from live prediction metrics."""
    predictions = prediction_service.get_all_predictions()

    flood_zones = []
    river_markers = []

    for p in predictions:
        district = p["district"]
        # Find coordinates for district
        lat = 26.1445
        lng = 91.7362
        if district == "Sivasagar":
            lat, lng = 26.9826, 94.6425
        elif district == "Jorhat":
            lat, lng = 26.7509, 94.2037
        elif district == "Golaghat":
            lat, lng = 26.5167, 93.9667
        elif district == "Cachar":
            lat, lng = 24.8333, 92.7667
        elif district == "Charaideo":
            lat, lng = 26.9000, 94.8800
        elif district == "Dibrugarh":
            lat, lng = 27.4728, 94.9120
        elif district == "Nagaon":
            lat, lng = 26.3463, 92.6840

        flood_zones.append(
            {
                "district": district,
                "coordinates": {"lat": lat, "lng": lng},
                "risk_level": p["risk_level"],
                "severity_score": p["severity_score"],
                "affected_radius_km": round(4.0 + (p["severity_score"] / 20.0), 1),
            }
        )

        is_above = p["water_level_m"] >= p["danger_mark_m"]
        river_markers.append(
            {
                "district": district,
                "river_name": p["river_name"],
                "coordinates": {"lat": lat, "lng": lng},
                "water_level_m": p["water_level_m"],
                "danger_mark_m": p["danger_mark_m"],
                "status": "Above Danger" if is_above else "Normal",
            }
        )

    return {
        "map_center": GUWAHATI_CENTER,
        "zoom_level": 9,
        "flood_zones": flood_zones,
        "river_markers": river_markers,
    }


def get_map_center() -> Dict[str, Any]:
    return GUWAHATI_CENTER


def get_flood_zones() -> List[Dict[str, Any]]:
    return get_map_data().get("flood_zones", [])


def get_flood_zone_by_district(district: str) -> Dict[str, Any]:
    zones = get_flood_zones()
    for z in zones:
        if z.get("district", "").lower() == district.lower():
            return z
    return {}


def get_river_markers() -> List[Dict[str, Any]]:
    return get_map_data().get("river_markers", [])


def get_rivers_above_danger_level() -> List[Dict[str, Any]]:
    return [r for r in get_river_markers() if r.get("status") == "Above Danger"]
