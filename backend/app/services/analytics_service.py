import logging
from typing import Any, Dict, List
from app.database.loader import load_json

logger = logging.getLogger(__name__)

FILENAME = "analytics.json"


def get_analytics_overview() -> Dict[str, Any]:
    """Return full analytics dataset."""
    data = load_json(FILENAME)
    if isinstance(data, dict) and data:
        return data

    return {
        "summary": {
            "total_incidents_logged": 42,
            "average_response_time_min": 33,
            "overall_ai_model_accuracy": "92%",
        },
        "monthly_trend": [
            {"month": "Feb", "incidents": 2},
            {"month": "Mar", "incidents": 4},
            {"month": "Apr", "incidents": 6},
            {"month": "May", "incidents": 9},
            {"month": "Jun", "incidents": 15},
            {"month": "Jul", "incidents": 22},
        ],
        "disaster_type_distribution": {
            "Flood": 65,
            "Heavy Rain & Waterlogging": 20,
            "Landslide": 10,
            "River Bank Erosion": 5,
        },
        "district_wise_impact": [
            {"district": "Sivasagar", "incidents": 14, "affected_people": 85000},
            {"district": "Cachar", "incidents": 11, "affected_people": 64000},
            {"district": "Golaghat", "incidents": 8, "affected_people": 42000},
            {"district": "Jorhat", "incidents": 6, "affected_people": 31000},
            {
                "district": "Kamrup Metropolitan",
                "incidents": 3,
                "affected_people": 23000,
            },
        ],
    }


def get_summary() -> Dict[str, Any]:
    return get_analytics_overview().get("summary", {})


def get_district_wise_impact() -> List[Dict[str, Any]]:
    return get_analytics_overview().get("district_wise_impact", [])


def get_monthly_trend() -> List[Dict[str, Any]]:
    data = load_json(FILENAME)
    if isinstance(data, dict) and "monthly_trend" in data:
        return data["monthly_trend"]
    return [
        {"month": "Feb", "incidents": 2},
        {"month": "Mar", "incidents": 4},
        {"month": "Apr", "incidents": 6},
        {"month": "May", "incidents": 9},
        {"month": "Jun", "incidents": 15},
        {"month": "Jul", "incidents": 22},
    ]


def get_disaster_type_distribution() -> Dict[str, Any]:
    return get_analytics_overview().get("disaster_type_distribution", {})


def get_district_impact_by_name(district: str) -> Dict[str, Any]:
    for entry in get_district_wise_impact():
        if entry.get("district", "").lower() == district.lower():
            return entry
    return {}
