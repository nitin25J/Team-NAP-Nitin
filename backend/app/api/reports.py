# backend/app/api/reports.py

import logging
from typing import Any, Dict, List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services import report_service

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/reports",
    tags=["Citizen Reports"],
)

@router.get("/", response_model=List[Dict[str, Any]])
def get_all_reports_route(db: Session = Depends(get_db)) -> List[Dict[str, Any]]:
    try:
        return report_service.get_all_reports(db)
    except Exception as exc:
        logger.exception("Failed to retrieve reports")
        raise HTTPException(status_code=500, detail="Internal server error") from exc

@router.get("/verified", response_model=List[Dict[str, Any]])
def get_verified_reports_route(db: Session = Depends(get_db)) -> List[Dict[str, Any]]:
    try:
        return report_service.get_verified_reports(db)
    except Exception as exc:
        logger.exception("Failed to retrieve verified reports")
        raise HTTPException(status_code=500, detail="Internal server error") from exc

@router.get("/{report_id}", response_model=Dict[str, Any])
def get_report_by_id_route(report_id: int, db: Session = Depends(get_db)) -> Dict[str, Any]:
    try:
        report = report_service.get_report_by_id(db, report_id)
        if report is None:
            raise HTTPException(status_code=404, detail="Report not found")
        return report
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Failed to retrieve report")
        raise HTTPException(status_code=500, detail="Internal server error") from exc
