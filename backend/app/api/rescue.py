# backend/app/api/rescue.py

import logging
from typing import Any, Dict, List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services import rescue_service

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/rescue",
    tags=["Rescue Teams"],
)

@router.get("/", response_model=List[Dict[str, Any]])
def get_all_teams_route(db: Session = Depends(get_db)) -> List[Dict[str, Any]]:
    try:
        return rescue_service.get_all_teams(db)
    except Exception as exc:
        logger.exception("Failed to retrieve rescue teams")
        raise HTTPException(status_code=500, detail="Internal server error") from exc

@router.get("/status/{status_val}", response_model=List[Dict[str, Any]])
def get_teams_by_status_route(status_val: str, db: Session = Depends(get_db)) -> List[Dict[str, Any]]:
    try:
        return rescue_service.get_teams_by_status(db, status_val)
    except Exception as exc:
        logger.exception("Failed to retrieve rescue teams by status")
        raise HTTPException(status_code=500, detail="Internal server error") from exc

@router.get("/{team_id}", response_model=Dict[str, Any])
def get_team_by_id_route(team_id: int, db: Session = Depends(get_db)) -> Dict[str, Any]:
    try:
        team = rescue_service.get_team_by_id(db, team_id)
        if team is None:
            raise HTTPException(status_code=404, detail="Team not found")
        return team
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Failed to retrieve team")
        raise HTTPException(status_code=500, detail="Internal server error") from exc
