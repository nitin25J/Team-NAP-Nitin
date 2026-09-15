import json
import logging
from datetime import datetime, timedelta
from pathlib import Path

from app.database.database import engine, Base, SessionLocal
from app.database.db_models import (
    HospitalModel,
    ShelterModel,
    RescueTeamModel,
    EmergencyAlertModel,
    CitizenReportModel,
    ResourceItemModel,
)

logger = logging.getLogger(__name__)

# Locate root datasets/ directory dynamically
_curr = Path(__file__).resolve()
DATASETS_DIR = _curr.parents[3] / "datasets" if (_curr.parents[3] / "datasets").exists() else _curr.parents[2] / "datasets"


def load_dataset_file(filename: str):
    """Utility to safely load JSON dataset from root datasets/ folder."""
    file_path = DATASETS_DIR / filename
    if file_path.exists():
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.warning("Could not read %s from datasets dir: %s", filename, e)
    return None


def init_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        # 1. Seed Hospitals
        if db.query(HospitalModel).count() == 0:
            hospitals_data = load_dataset_file("assam_hospitals_dataset.json")
            if hospitals_data:
                hospitals = [
                    HospitalModel(
                        name=item["name"],
                        district=item["district"],
                        beds_available=item.get("beds_available", 0),
                        beds_total=item.get("beds_total", 100),
                        icu_available=item.get("icu_available", item.get("icu_beds", 0)),
                        icu_total=item.get("icu_total", 20),
                        lat=item.get("lat"),
                        lng=item.get("lng"),
                        contact=item.get("contact", "+91 361 2529457"),
                        status=item.get("status", "Operational"),
                    )
                    for item in hospitals_data
                ]
                db.add_all(hospitals)
            else:
                logger.error("Hospitals dataset not found or empty.")

        # 2. Seed Shelters
        if db.query(ShelterModel).count() == 0:
            shelters_data = load_dataset_file("assam_shelters_dataset.json")
            if shelters_data:
                shelters = [
                    ShelterModel(
                        name=item["name"],
                        district=item["district"],
                        capacity=item.get("capacity", 500),
                        occupancy=item.get("occupancy", 0),
                        lat=item.get("lat"),
                        lng=item.get("lng"),
                    )
                    for item in shelters_data
                ]
                db.add_all(shelters)
            else:
                logger.error("Shelters dataset not found or empty.")

        # 3. Seed Rescue Teams
        if db.query(RescueTeamModel).count() == 0:
            rescue_data = load_dataset_file("assam_rescue_units_dataset.json")
            if rescue_data:
                teams = [
                    RescueTeamModel(
                        team_id=item.get("team_id", f"TEAM-{item.get('id')}"),
                        name=item["name"],
                        type=item.get("type", "NDRF"),
                        district=item["district"],
                        personnel_count=item.get("personnel_count", item.get("members", 10)),
                        status=item.get("status", "Deployed"),
                        lat=item.get("lat"),
                        lng=item.get("lng"),
                    )
                    for item in rescue_data
                ]
                db.add_all(teams)
            else:
                logger.error("Rescue teams dataset not found or empty.")

        # 4. Seed Emergency Alerts
        if db.query(EmergencyAlertModel).count() == 0:
            now = datetime.utcnow()
            alerts_data = load_dataset_file("assam_emergency_alerts_dataset.json")
            if alerts_data:
                alerts = [
                    EmergencyAlertModel(
                        alert_id=item.get("alert_id", f"ALT-{idx+101}"),
                        type=item.get("type", "Flash Flood Warning"),
                        severity=item.get("severity", "Critical"),
                        district=item["district"],
                        river=item.get("river"),
                        message=item["message"],
                        issued_by=item.get("issued_by", "Assam State Disaster Management Authority"),
                        issued_at=now - timedelta(hours=idx + 1),
                        valid_until=now + timedelta(hours=12),
                        status=item.get("status", "Active"),
                    )
                    for idx, item in enumerate(alerts_data)
                ]
                db.add_all(alerts)
            else:
                logger.error("Emergency alerts dataset not found or empty.")

        # 5. Seed Citizen Reports
        if db.query(CitizenReportModel).count() == 0:
            now = datetime.utcnow()
            reports_data = load_dataset_file("assam_citizen_reports_dataset.json")
            if reports_data:
                reports = [
                    CitizenReportModel(
                        report_id=item.get("report_id", f"REP-{idx+901}"),
                        reporter_name=item.get("reporter_name", item.get("user", "Anonymous")),
                        type=item.get("type", "Flooding"),
                        location=item.get("location", item.get("district")),
                        district=item.get("district", "Assam"),
                        description=item.get("description", ""),
                        status=item.get("status", "Verified"),
                        media_attached=item.get("media_attached", True),
                        submitted_at=now - timedelta(minutes=(idx + 1) * 20),
                    )
                    for idx, item in enumerate(reports_data)
                ]
                db.add_all(reports)
            else:
                logger.error("Citizen reports dataset not found or empty.")

        # 6. Seed Resource Items
        if db.query(ResourceItemModel).count() == 0:
            resources_data = load_dataset_file("assam_disaster_resources_dataset.json")
            if resources_data:
                resources = [
                    ResourceItemModel(
                        name=item["name"],
                        icon=item.get("icon", "ti-package"),
                        have=item.get("have", 0),
                        total=item.get("total", 100),
                        color=item.get("color", "var(--safe)"),
                    )
                    for item in resources_data
                ]
                db.add_all(resources)
            else:
                logger.error("Resource items dataset not found or empty.")

        db.commit()
        logger.info("Successfully initialized and seeded database from datasets folder.")
    except Exception as e:
        db.rollback()
        logger.error("Error seeding database: %s", e)
    finally:
        db.close()


if __name__ == "__main__":
    init_db()
    print("Database initialized and seeded with rich Assam disaster intelligence dataset.")
