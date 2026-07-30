import logging
from typing import Any, Dict, List, Optional

from app.database.loader import load_json

logger = logging.getLogger(__name__)

FILENAME = "alerts.json"


def get_all_alerts() -> List[Dict[str, Any]]:
    """Return all alerts from the database."""
    data = load_json(FILENAME)
    alerts = data.get("alerts", []) if isinstance(data, dict) else []
    return alerts


def get_active_alerts() -> List[Dict[str, Any]]:
    """Return only alerts with status 'Active'."""
    alerts = get_all_alerts()
    return [alert for alert in alerts if alert.get("status") == "Active"]


def get_alert_by_id(alert_id: str) -> Optional[Dict[str, Any]]:
    """Return a single alert matching the given ID."""
    alerts = get_all_alerts()
    for alert in alerts:
        if alert.get("id") == alert_id:
            return alert
    logger.warning("Alert not found: %s", alert_id)
    return None


def get_alerts_by_district(district: str) -> List[Dict[str, Any]]:
    """Return alerts filtered by district (case-insensitive)."""
    alerts = get_all_alerts()
    return [
        alert for alert in alerts
        if alert.get("district", "").lower() == district.lower()
    ]


def get_alerts_by_severity(severity: str) -> List[Dict[str, Any]]:
    """Return alerts filtered by severity level (case-insensitive)."""
    alerts = get_all_alerts()
    return [
        alert for alert in alerts
        if alert.get("severity", "").lower() == severity.lower()
    ]