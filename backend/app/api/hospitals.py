# backend/app/api/hospitals.py
import logging
from typing import Any, Dict, List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services import hospital_service

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/hospitals",
    tags=["Hospitals"],
)

@router.get("/", response_model=List[Dict[str, Any]])
def get_all_hospitals_route(db: Session = Depends(get_db)) -> List[Dict[str, Any]]:
    """Return all hospitals."""
    try:
        return hospital_service.get_all_hospitals(db)
    except Exception as exc:
        logger.exception("Failed to retrieve hospitals")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc

@router.get("/district/{district}", response_model=List[Dict[str, Any]])
def get_hospitals_by_district_route(
    district: str,
    db: Session = Depends(get_db)
) -> List[Dict[str, Any]]:
    """Return hospitals in a district."""
    try:
        return hospital_service.get_hospitals_by_district(db, district)
    except Exception as exc:
        logger.exception("Failed to retrieve district hospitals")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc

@router.get("/{hospital_id}", response_model=Dict[str, Any])
def get_hospital_by_id_route(
    hospital_id: int,
    db: Session = Depends(get_db)
) -> Dict[str, Any]:
    """Return a hospital by ID."""
    try:
        hospital = hospital_service.get_hospital_by_id(db, hospital_id)
        if hospital is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Hospital not found",
            )
        return hospital
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Failed to retrieve hospital")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc
