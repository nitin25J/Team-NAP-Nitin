import logging
from typing import Any, Dict, List, Optional
from datetime import datetime, timedelta
from app.database.loader import load_json
from app.database.database import SessionLocal
from app.database.db_models import EmergencyAlertModel

logger = logging.getLogger(__name__)

FILENAME = "alerts.json"


def get_all_alerts() -> List[Dict[str, Any]]:
    """Return all emergency alerts from SQLite database."""
    data = load_json(FILENAME)
    if isinstance(data, list):
        return data
    elif isinstance(data, dict):
        return data.get("alerts", [])
    return []


def get_active_alerts() -> List[Dict[str, Any]]:
    """Return active alerts."""
    alerts = get_all_alerts()
    return [alert for alert in alerts if (alert.get("status") or "").lower() == "active"]


def get_alert_by_id(alert_id: str) -> Optional[Dict[str, Any]]:
    """Return alert matching ID."""
    alerts = get_all_alerts()
    for alert in alerts:
        if alert.get("alert_id") == alert_id or str(alert.get("id")) == str(alert_id):
            return alert
    return None


def get_alerts_by_district(district: str) -> List[Dict[str, Any]]:
    """Return alerts filtered by district."""
    alerts = get_all_alerts()
    return [
        alert for alert in alerts
        if (alert.get("district") or "").lower() == district.lower()
    ]


def get_alerts_by_severity(severity: str) -> List[Dict[str, Any]]:
    """Return alerts filtered by severity."""
    alerts = get_all_alerts()
    return [
        alert for alert in alerts
        if (alert.get("severity") or "").lower() == severity.lower()
    ]


def create_alert(new_alert: Dict[str, Any]) -> Dict[str, Any]:
    """Create a new emergency alert in SQLite database."""
    db = SessionLocal()
    try:
        now = datetime.utcnow()
        valid_hours = int(new_alert.get("valid_hours", 12))
        alert_obj = EmergencyAlertModel(
            alert_id=f"ALT-{int(now.timestamp())}",
            type=new_alert.get("type", "Emergency Disaster Advisory"),
            severity=new_alert.get("severity", "Severe"),
            district=new_alert.get("district", "General"),
            river=new_alert.get("river", "Regional River Basin"),
            message=new_alert.get("message", "Immediate public caution advised."),
            issued_by=new_alert.get("issued_by", "Assam State Disaster Control Room"),
            issued_at=now,
            valid_until=now + timedelta(hours=valid_hours),
            status="Active"
        )
        db.add(alert_obj)
        db.commit()
        db.refresh(alert_obj)
        return alert_obj.to_dict()
    except Exception as e:
        db.rollback()
        logger.exception("Failed to create alert: %s", e)
        raise e
    finally:
        db.close()