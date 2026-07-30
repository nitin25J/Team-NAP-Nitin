import logging
from typing import Any, Dict, List, Optional

from app.database.loader import load_json

logger = logging.getLogger(__name__)

FILENAME = "satellite.json"


def get_all_satellite_analysis() -> List[Dict[str, Any]]:
    """Return all satellite analysis records."""
    data = load_json(FILENAME)
    records = data.get("satellite_analysis", []) if isinstance(data, dict) else []
    return records


def get_satellite_analysis_by_district(district: str) -> Optional[Dict[str, Any]]:
    """Return satellite analysis for a specific district."""
    records = get_all_satellite_analysis()
    for record in records:
        if record.get("district", "").lower() == district.lower():
            return record
    logger.warning("Satellite analysis not found for district: %s", district)
    return None


def get_significant_flood_changes(threshold_percent: float = 10.0) -> List[Dict[str, Any]]:
    """Return districts where flood extent change exceeds the given threshold."""
    records = get_all_satellite_analysis()
    return [
        r for r in records
        if isinstance(r.get("change_from_previous_capture_percent"), (int, float))
        and r["change_from_previous_capture_percent"] >= threshold_percent
    ]


def get_total_flood_extent() -> float:
    """Return the combined flood extent (sq km) across all analyzed districts."""
    records = get_all_satellite_analysis()
    total = sum(
        r.get("flood_extent_sq_km", 0)
        for r in records
        if isinstance(r.get("flood_extent_sq_km"), (int, float))
    )
    return round(total, 2)