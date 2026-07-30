import logging
from typing import Any, Dict, List

from app.database.loader import load_json

logger = logging.getLogger(__name__)

FILENAME = "map.json"


def get_map_data() -> Dict[str, Any]:
    """Return the full disaster map dataset."""
    data = load_json(FILENAME)
    if not isinstance(data, dict):
        logger.warning("Map data malformed or empty")
        return {}
    return data


def get_map_center() -> Dict[str, Any]:
    """Return the default map center coordinates."""
    data = get_map_data()
    return data.get("map_center", {})


def get_flood_zones() -> List[Dict[str, Any]]:
    """Return all flood zone markers."""
    data = get_map_data()
    return data.get("flood_zones", [])


def get_flood_zone_by_district(district: str) -> Dict[str, Any]:
    """Return flood zone information for a specific district."""
    zones = get_flood_zones()
    for zone in zones:
        if zone.get("district", "").lower() == district.lower():
            return zone
    logger.warning("Flood zone not found for district: %s", district)
    return {}


def get_river_markers() -> List[Dict[str, Any]]:
    """Return river level markers for the map."""
    data = get_map_data()
    return data.get("river_markers", [])


def get_rivers_above_danger_level() -> List[Dict[str, Any]]:
    """Return river markers currently above danger level."""
    rivers = get_river_markers()
    return [r for r in rivers if r.get("status") == "Above Danger"]