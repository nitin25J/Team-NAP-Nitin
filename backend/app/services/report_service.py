import logging
from typing import Any, Dict, List, Optional
from datetime import datetime
from app.database.loader import load_json
from app.database.database import SessionLocal
from app.database.db_models import CitizenReportModel

logger = logging.getLogger(__name__)

FILENAME = "reports.json"


def get_all_reports() -> List[Dict[str, Any]]:
    """Return all citizen reports from SQLite database."""
    data = load_json(FILENAME)
    if isinstance(data, list):
        return data
    elif isinstance(data, dict):
        return data.get("citizen_reports", [])
    return []


def get_report_by_id(report_id: str) -> Optional[Dict[str, Any]]:
    """Return report matching ID."""
    reports = get_all_reports()
    for report in reports:
        if report.get("report_id") == report_id or str(report.get("id")) == str(
            report_id
        ):
            return report
    return None


def get_reports_by_district(district: str) -> List[Dict[str, Any]]:
    """Return reports filtered by district."""
    reports = get_all_reports()
    return [
        report
        for report in reports
        if (report.get("district") or "").lower() == district.lower()
    ]


def get_reports_by_status(status: str) -> List[Dict[str, Any]]:
    """Return reports filtered by review status."""
    reports = get_all_reports()
    return [
        report
        for report in reports
        if (report.get("status") or "").lower() == status.lower()
    ]


def add_report(new_report: Dict[str, Any]) -> bool:
    """Save a new citizen report into SQLite database."""
    db = SessionLocal()
    try:
        now = datetime.utcnow()
        report_obj = CitizenReportModel(
            report_id=f"REP-{int(now.timestamp())}",
            reporter_name=new_report.get("reporter_name", "Anonymous Citizen"),
            type=new_report.get("type", "Disaster Distress"),
            location=new_report.get("location", "Unspecified Ward"),
            district=new_report.get("district", "Sivasagar"),
            description=new_report.get("description", ""),
            status="Pending Review",
            media_attached=bool(new_report.get("media_attached", False)),
            submitted_at=now,
        )
        db.add(report_obj)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        logger.exception("Failed to insert citizen report: %s", e)
        return False
    finally:
        db.close()
