# backend/app/services/hospital_service.py

from typing import Any, Dict, List, Optional
from sqlalchemy.orm import Session
from app.database.models import Hospital

def get_all_hospitals(db: Session) -> List[Dict[str, Any]]:
    hospitals = db.query(Hospital).all()
    return [
        {
            "id": h.id,
            "name": h.name,
            "district": h.district,
            "beds_total": h.beds_total,
            "beds_available": h.beds_available,
            "icu_total": h.icu_total,
            "icu_available": h.icu_available,
            "oxygen_available": h.oxygen_available,
            "status": h.status,
            "last_updated": h.last_updated.isoformat() if h.last_updated else None,
        }
        for h in hospitals
    ]

def get_hospital_by_id(db: Session, hospital_id: int) -> Optional[Dict[str, Any]]:
    h = db.query(Hospital).filter(Hospital.id == hospital_id).first()
    if h:
        return {
            "id": h.id,
            "name": h.name,
            "district": h.district,
            "beds_total": h.beds_total,
            "beds_available": h.beds_available,
            "icu_total": h.icu_total,
            "icu_available": h.icu_available,
            "oxygen_available": h.oxygen_available,
            "status": h.status,
            "last_updated": h.last_updated.isoformat() if h.last_updated else None,
        }
    return None

def get_hospitals_by_district(db: Session, district: str) -> List[Dict[str, Any]]:
    hospitals = db.query(Hospital).filter(Hospital.district.ilike(f"%{district}%")).all()
    return [
        {
            "id": h.id,
            "name": h.name,
            "district": h.district,
            "beds_total": h.beds_total,
            "beds_available": h.beds_available,
            "icu_total": h.icu_total,
            "icu_available": h.icu_available,
            "oxygen_available": h.oxygen_available,
            "status": h.status,
            "last_updated": h.last_updated.isoformat() if h.last_updated else None,
        }
        for h in hospitals
    ]
