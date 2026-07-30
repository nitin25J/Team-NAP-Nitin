import logging
from typing import Any, Dict, List

from app.database.loader import load_json

logger = logging.getLogger(__name__)

FILENAME = "resources.json"


def get_resource_data() -> Dict[str, Any]:
    """Return the full resource inventory dataset."""
    data = load_json(FILENAME)
    if not isinstance(data, dict):
        logger.warning("Resource data malformed or empty")
        return {}
    return data


def get_inventory_summary() -> Dict[str, Any]:
    """Return the state-wide inventory summary."""
    data = get_resource_data()
    return data.get("inventory_summary", {})


def get_district_resources() -> List[Dict[str, Any]]:
    """Return resource allocation for all districts."""
    data = get_resource_data()
    return data.get("district_resources", [])


def get_resources_by_district(district: str) -> Dict[str, Any]:
    """Return resource allocation for a specific district."""
    districts = get_district_resources()
    for entry in districts:
        if entry.get("district", "").lower() == district.lower():
            return entry
    logger.warning("Resources not found for district: %s", district)
    return {}


def get_shelters_by_district(district: str) -> List[Dict[str, Any]]:
    """Return the list of shelters for a specific district."""
    district_data = get_resources_by_district(district)
    return district_data.get("shelters", [])


def get_all_shelters() -> List[Dict[str, Any]]:
    """Return all shelters across all districts, tagged with district name."""
    districts = get_district_resources()
    all_shelters: List[Dict[str, Any]] = []
    for entry in districts:
        district_name = entry.get("district")
        for shelter in entry.get("shelters", []):
            shelter_with_district = dict(shelter)
            shelter_with_district["district"] = district_name
            all_shelters.append(shelter_with_district)
    return all_shelters