import json
import logging
from pathlib import Path
from typing import Any, List, Union

from app.database.database import SessionLocal
from app.database.db_models import (
    HospitalModel,
    ShelterModel,
    RescueTeamModel,
    EmergencyAlertModel,
    CitizenReportModel,
    ResourceItemModel,
)

logger = logging.getLogger(__name__)

DATABASE_DIR = Path(__file__).resolve().parent / "dummy"
_curr = Path(__file__).resolve()
DATASETS_DIR = _curr.parents[3] / "datasets" if (_curr.parents[3] / "datasets").exists() else _curr.parents[2] / "datasets"

FILE_TO_DATASET_MAP = {
    "hospitals.json": "assam_hospitals_dataset.json",
    "rescue.json": "assam_rescue_units_dataset.json",
    "alerts.json": "assam_emergency_alerts_dataset.json",
    "reports.json": "assam_citizen_reports_dataset.json",
    "resources.json": "assam_disaster_resources_dataset.json",
    "shelters.json": "assam_shelters_dataset.json",
}


def load_json(filename: str) -> Union[List[Any], dict]:
    """
    Load data dynamically from SQLite database based on target entity filename.
    Falls back to root datasets/ folder or dummy files if DB query returns empty.
    """
    db = SessionLocal()
    try:
        if filename == "hospitals.json":
            hospitals = db.query(HospitalModel).all()
            if hospitals:
                return [h.to_dict() for h in hospitals]

        elif filename == "rescue.json":
            teams = db.query(RescueTeamModel).all()
            if teams:
                return [t.to_dict() for t in teams]

        elif filename == "alerts.json":
            alerts = db.query(EmergencyAlertModel).all()
            if alerts:
                return [a.to_dict() for a in alerts]

        elif filename == "reports.json":
            reports = db.query(CitizenReportModel).all()
            if reports:
                return [r.to_dict() for r in reports]

        elif filename == "resources.json":
            resources = db.query(ResourceItemModel).all()
            shelters = db.query(ShelterModel).all()
            if resources or shelters:
                return {
                    "inventory": [r.to_dict() for r in resources],
                    "shelters": [s.to_dict() for s in shelters],
                }

        elif filename == "settings.json":
            return {
                "theme": "dark",
                "language": "English",
                "notifications": {
                    "critical_alerts": True,
                    "shelter_warnings": True,
                    "weekly_digest": False,
                },
                "user": {
                    "name": "Nitin Sharma",
                    "role": "Director General, NDRF",
                    "state": "Assam",
                },
            }

        # Fallback 1: Root datasets/ directory
        if filename in FILE_TO_DATASET_MAP:
            ds_path = DATASETS_DIR / FILE_TO_DATASET_MAP[filename]
            if ds_path.exists():
                with ds_path.open("r", encoding="utf-8") as f:
                    return json.load(f)

        # Fallback 2: Local dummy JSON file
        file_path = DATABASE_DIR / filename
        if file_path.exists():
            with file_path.open("r", encoding="utf-8") as f:
                return json.load(f)

        return []

    except Exception as e:
        logger.exception("Error loading entity data for %s: %s", filename, e)
        # Attempt direct JSON fallback on exception
        if filename in FILE_TO_DATASET_MAP:
            ds_path = DATASETS_DIR / FILE_TO_DATASET_MAP[filename]
            if ds_path.exists():
                try:
                    with ds_path.open("r", encoding="utf-8") as f:
                        return json.load(f)
                except Exception:
                    pass
        return []
    finally:
        db.close()


def save_json(filename: str, data: Any) -> bool:
    """
    Save JSON data or update database entities.
    """
    file_path = DATABASE_DIR / filename
    try:
        DATABASE_DIR.mkdir(parents=True, exist_ok=True)
        with file_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        logger.exception("Error saving file %s: %s", filename, e)
        return False
