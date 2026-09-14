# backend/app/services/rescue_service.py

from typing import Any, Dict, List, Optional
from sqlalchemy.orm import Session
from app.database.models import RescueTeam

def get_all_teams(db: Session) -> List[Dict[str, Any]]:
    teams = db.query(RescueTeam).all()
    return [
        {
            "id": t.id,
            "name": t.name,
            "type": t.type,
            "location": t.location,
            "personnel_count": t.personnel_count,
            "status": t.status,
            "last_updated": t.last_updated.isoformat() if t.last_updated else None,
        }
        for t in teams
    ]

def get_team_by_id(db: Session, team_id: int) -> Optional[Dict[str, Any]]:
    t = db.query(RescueTeam).filter(RescueTeam.id == team_id).first()
    if t:
        return {
            "id": t.id,
            "name": t.name,
            "type": t.type,
            "location": t.location,
            "personnel_count": t.personnel_count,
            "status": t.status,
            "last_updated": t.last_updated.isoformat() if t.last_updated else None,
        }
    return None

def get_teams_by_status(db: Session, status: str) -> List[Dict[str, Any]]:
    teams = db.query(RescueTeam).filter(RescueTeam.status.ilike(f"%{status}%")).all()
    return [
        {
            "id": t.id,
            "name": t.name,
            "type": t.type,
            "location": t.location,
            "personnel_count": t.personnel_count,
            "status": t.status,
            "last_updated": t.last_updated.isoformat() if t.last_updated else None,
        }
        for t in teams
    ]
