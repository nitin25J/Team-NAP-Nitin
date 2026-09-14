# backend/app/api/dashboard.py

import logging
from typing import Any, Dict, List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services import dashboard_service

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)

@router.get("/", response_model=Dict[str, Any])
def get_dashboard_data_route(db: Session = Depends(get_db)) -> Dict[str, Any]:
    try:
        return dashboard_service.get_dashboard_data(db)
    except Exception as exc:
        logger.exception("Failed to retrieve dashboard data")
        raise HTTPException(status_code=500, detail="Internal server error") from exc

@router.get("/overview", response_model=Dict[str, Any])
def get_overview_stats_route(db: Session = Depends(get_db)) -> Dict[str, Any]:
    try:
        return dashboard_service.get_overview_stats(db)
    except Exception as exc:
        logger.exception("Failed to retrieve overview statistics")
        raise HTTPException(status_code=500, detail="Internal server error") from exc

@router.get("/top-districts", response_model=List[Dict[str, Any]])
def get_top_affected_districts_route(db: Session = Depends(get_db)) -> List[Dict[str, Any]]:
    try:
        return dashboard_service.get_top_affected_districts(db)
    except Exception as exc:
        logger.exception("Failed to retrieve top affected districts")
        raise HTTPException(status_code=500, detail="Internal server error") from exc

@router.get("/quick-links", response_model=List[Dict[str, Any]])
def get_quick_links_route(db: Session = Depends(get_db)) -> List[Dict[str, Any]]:
    try:
        return dashboard_service.get_quick_links(db)
    except Exception as exc:
        logger.exception("Failed to retrieve quick links")
        raise HTTPException(status_code=500, detail="Internal server error") from exc

@router.get("/recent-activity", response_model=List[Dict[str, Any]])
def get_recent_activity_route(db: Session = Depends(get_db)) -> List[Dict[str, Any]]:
    try:
        return dashboard_service.get_recent_activity(db)
    except Exception as exc:
        logger.exception("Failed to retrieve recent activity")
        raise HTTPException(status_code=500, detail="Internal server error") from exc
