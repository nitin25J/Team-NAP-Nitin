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


def load_json(filename: str) -> Union[List[Any], dict]:
    """
    Load data dynamically from SQLite database based on target entity filename.
    Falls back to dummy file if file is non-entity config or during transition.
    """
    db = SessionLocal()
    try:
        if filename == "hospitals.json":
            hospitals = db.query(HospitalModel).all()
            return [h.to_dict() for h in hospitals]

        elif filename == "rescue.json":
            teams = db.query(RescueTeamModel).all()
            return [t.to_dict() for t in teams]

        elif filename == "alerts.json":
            alerts = db.query(EmergencyAlertModel).all()
            return [a.to_dict() for a in alerts]

        elif filename == "reports.json":
            reports = db.query(CitizenReportModel).all()
            return [r.to_dict() for r in reports]

        elif filename == "resources.json":
            resources = db.query(ResourceItemModel).all()
            shelters = db.query(ShelterModel).all()
            return {
                "inventory": [r.to_dict() for r in resources],
                "shelters": [s.to_dict() for s in shelters]
            }

        elif filename == "settings.json":
            return {
                "theme": "dark",
                "language": "English",
                "notifications": {"critical_alerts": True, "shelter_warnings": True, "weekly_digest": False},
                "user": {"name": "Nitin Sharma", "role": "Director General, NDRF", "state": "Assam"}
            }

        # Fallback to local JSON file if exists
        file_path = DATABASE_DIR / filename
        if file_path.exists():
            with file_path.open("r", encoding="utf-8") as f:
                return json.load(f)

        return []

    except Exception as e:
        logger.exception("Error loading entity data for %s: %s", filename, e)
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