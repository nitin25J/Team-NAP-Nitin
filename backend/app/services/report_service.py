# backend/app/services/report_service.py

from typing import Any, Dict, List, Optional
from sqlalchemy.orm import Session
from app.database.models import Incident

def get_all_reports(db: Session) -> List[Dict[str, Any]]:
    incidents = db.query(Incident).order_by(Incident.timestamp.desc()).all()
    return [
        {
            "id": i.id,
            "reporter_name": i.reporter_name,
            "location": i.location,
            "description": i.description,
            "severity": i.severity,
            "image_url": i.image_url,
            "verified": i.verified,
            "status": i.status,
            "timestamp": i.timestamp.isoformat() if i.timestamp else None,
        }
        for i in incidents
    ]

def get_report_by_id(db: Session, report_id: int) -> Optional[Dict[str, Any]]:
    i = db.query(Incident).filter(Incident.id == report_id).first()
    if i:
        return {
            "id": i.id,
            "reporter_name": i.reporter_name,
            "location": i.location,
            "description": i.description,
            "severity": i.severity,
            "image_url": i.image_url,
            "verified": i.verified,
            "status": i.status,
            "timestamp": i.timestamp.isoformat() if i.timestamp else None,
        }
    return None

def get_verified_reports(db: Session) -> List[Dict[str, Any]]:
    incidents = db.query(Incident).filter(Incident.verified == True).order_by(Incident.timestamp.desc()).all()
    return [
        {
            "id": i.id,
            "reporter_name": i.reporter_name,
            "location": i.location,
            "description": i.description,
            "severity": i.severity,
            "image_url": i.image_url,
            "verified": i.verified,
            "status": i.status,
            "timestamp": i.timestamp.isoformat() if i.timestamp else None,
        }
        for i in incidents
    ]
