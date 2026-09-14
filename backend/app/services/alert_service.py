import logging
from typing import Any, Dict, List, Optional
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

MOCK_ALERTS = [
    {
        "id": "ALT-1",
        "alert_id": "ALT-1",
        "type": "Emergency Disaster Advisory",
        "severity": "Severe",
        "district": "Majuli",
        "river": "Brahmaputra",
        "message": "Immediate public caution advised. River levels exceeding danger mark by 1.2m.",
        "issued_by": "Assam State Disaster Control Room",
        "issued_at": datetime.utcnow().isoformat(),
        "valid_until": (datetime.utcnow() + timedelta(hours=12)).isoformat(),
        "status": "Active",
    },
    {
        "id": "ALT-2",
        "alert_id": "ALT-2",
        "type": "Evacuation Warning",
        "severity": "Critical",
        "district": "Cachar",
        "river": "Barak",
        "message": "Evacuation in progress for low-lying areas. Follow SDRF instructions.",
        "issued_by": "District Disaster Management Authority",
        "issued_at": datetime.utcnow().isoformat(),
        "valid_until": (datetime.utcnow() + timedelta(hours=24)).isoformat(),
        "status": "Active",
    }
]

def get_all_alerts() -> List[Dict[str, Any]]:
    return MOCK_ALERTS

def get_active_alerts() -> List[Dict[str, Any]]:
    return [a for a in MOCK_ALERTS if a["status"].lower() == "active"]

def get_alert_by_id(alert_id: str) -> Optional[Dict[str, Any]]:
    for a in MOCK_ALERTS:
        if str(a["id"]) == str(alert_id) or str(a["alert_id"]) == str(alert_id):
            return a
    return None

def get_alerts_by_district(district: str) -> List[Dict[str, Any]]:
    return [a for a in MOCK_ALERTS if a["district"].lower() == district.lower()]

def get_alerts_by_severity(severity: str) -> List[Dict[str, Any]]:
    return [a for a in MOCK_ALERTS if a["severity"].lower() == severity.lower()]
