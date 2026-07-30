import logging
from typing import Any, Dict, List, Optional

from app.database.loader import load_json, save_json

logger = logging.getLogger(__name__)

FILENAME = "reports.json"


def get_all_reports() -> List[Dict[str, Any]]:
    """Return all citizen reports from the database."""
    data = load_json(FILENAME)
    reports = data.get("citizen_reports", []) if isinstance(data, dict) else []
    return reports


def get_report_by_id(report_id: str) -> Optional[Dict[str, Any]]:
    """Return a single citizen report matching the given ID."""
    reports = get_all_reports()
    for report in reports:
        if report.get("id") == report_id:
            return report
    logger.warning("Report not found: %s", report_id)
    return None


def get_reports_by_district(district: str) -> List[Dict[str, Any]]:
    """Return citizen reports filtered by district (case-insensitive)."""
    reports = get_all_reports()
    return [
        report for report in reports
        if report.get("district", "").lower() == district.lower()
    ]


def get_reports_by_status(status: str) -> List[Dict[str, Any]]:
    """Return citizen reports filtered by status (case-insensitive)."""
    reports = get_all_reports()
    return [
        report for report in reports
        if report.get("status", "").lower() == status.lower()
    ]


def add_report(new_report: Dict[str, Any]) -> bool:
    """
    Append a new citizen report and persist it to the database.
    Returns True on success, False on failure.
    """
    data = load_json(FILENAME)
    if not isinstance(data, dict):
        logger.warning("Reports data malformed, reinitializing structure")
        data = {"citizen_reports": []}

    reports = data.get("citizen_reports", [])
    reports.append(new_report)
    data["citizen_reports"] = reports

    success = save_json(FILENAME, data)
    if not success:
        logger.error("Failed to save new report: %s", new_report.get("id"))
    return success