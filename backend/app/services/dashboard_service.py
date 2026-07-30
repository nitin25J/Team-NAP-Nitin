import logging
from typing import Any, Dict, List

from app.database.loader import load_json

logger = logging.getLogger(__name__)

FILENAME = "dashboard.json"


def get_dashboard_data() -> Dict[str, Any]:
    """
    Return complete dashboard data.
    """
    data = load_json(FILENAME)

    if not isinstance(data, dict):
        logger.warning("Invalid dashboard data format.")
        return {}

    return data


def get_overview_stats() -> Dict[str, Any]:
    """
    Return overview statistics.
    """
    data = get_dashboard_data()
    return data.get("overview", {})


def get_top_affected_districts() -> List[Dict[str, Any]]:
    """
    Return top affected districts.
    """
    data = get_dashboard_data()
    return data.get("top_districts", [])


def get_quick_links() -> List[Dict[str, Any]]:
    """
    Return dashboard quick links.
    """
    data = get_dashboard_data()
    return data.get("quick_links", [])


def get_recent_activity() -> List[Dict[str, Any]]:
    """
    Return recent activity.
    """
    data = get_dashboard_data()
    return data.get("recent_activity", [])