import logging
from typing import Any, Dict, List, Optional
from app.database.loader import load_json

logger = logging.getLogger(__name__)

FILENAME = "hospitals.json"


def get_all_hospitals() -> List[Dict[str, Any]]:
    """Return all hospitals from SQLite database."""
    data = load_json(FILENAME)
    if isinstance(data, list):
        return data
    elif isinstance(data, dict):
        return data.get("hospitals", [])
    return []


def get_hospital_by_id(hospital_id: str) -> Optional[Dict[str, Any]]:
    """Return a single hospital matching given ID."""
    hospitals = get_all_hospitals()
    for hospital in hospitals:
        if str(hospital.get("id")) == str(hospital_id):
            return hospital
    return None


def get_hospitals_by_district(district: str) -> List[Dict[str, Any]]:
    """Return hospitals filtered by district."""
    hospitals = get_all_hospitals()
    return [
        hospital
        for hospital in hospitals
        if hospital.get("district", "").lower() == district.lower()
    ]


def get_flood_ready_hospitals() -> List[Dict[str, Any]]:
    """Return hospitals marked as flood-response ready."""
    hospitals = get_all_hospitals()
    return [h for h in hospitals if h.get("beds_available", 0) > 0]


def get_hospitals_with_available_beds(min_beds: int = 1) -> List[Dict[str, Any]]:
    """Return hospitals with available beds."""
    hospitals = get_all_hospitals()
    return [
        h
        for h in hospitals
        if isinstance(h.get("beds_available"), int) and h["beds_available"] >= min_beds
    ]
