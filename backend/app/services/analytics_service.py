import logging
from typing import Any, Dict, List

from app.database.loader import load_json

logger = logging.getLogger(__name__)

FILENAME = "analytics.json"


def get_analytics_overview() -> Dict[str, Any]:
    """Return the full analytics dataset."""
    data = load_json(FILENAME)
    if not isinstance(data, dict):
        logger.warning("Analytics data malformed or empty")
        return {}
    return data


def get_summary() -> Dict[str, Any]:
    """Return the summary statistics block."""
    data = get_analytics_overview()
    return data.get("summary", {})


def get_district_wise_impact() -> List[Dict[str, Any]]:
    """Return district-wise impact analytics."""
    data = get_analytics_overview()
    return data.get("district_wise_impact", [])


def get_monthly_trend() -> List[Dict[str, Any]]:
    """Return monthly trend analytics."""
    data = get_analytics_overview()
    return data.get("monthly_trend", [])


def get_disaster_type_distribution() -> Dict[str, Any]:
    """Return disaster type distribution percentages."""
    data = get_analytics_overview()
    return data.get("disaster_type_distribution", {})


def get_district_impact_by_name(district: str) -> Dict[str, Any]:
    """Return impact analytics for a specific district."""
    districts = get_district_wise_impact()
    for entry in districts:
        if entry.get("district", "").lower() == district.lower():
            return entry
    logger.warning("District analytics not found: %s", district)
    return {}