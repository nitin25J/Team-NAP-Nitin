# backend/app/api/satellite.py

import logging
from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, Query, status

from app.services import satellite_service

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/satellite",
    tags=["Satellite"],
)


@router.get("/", response_model=List[Dict[str, Any]])
def get_all_satellite_analysis_route() -> List[Dict[str, Any]]:
    """Return all satellite analysis records."""
    try:
        return satellite_service.get_all_satellite_analysis()

    except Exception as exc:
        logger.exception("Failed to retrieve satellite analysis")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/total-extent", response_model=Dict[str, float])
def get_total_flood_extent_route() -> Dict[str, float]:
    """Return total flood extent across all districts."""
    try:
        total = satellite_service.get_total_flood_extent()

        return {
            "total_flood_extent_sq_km": total,
        }

    except Exception as exc:
        logger.exception("Failed to retrieve total flood extent")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/significant-changes", response_model=List[Dict[str, Any]])
def get_significant_flood_changes_route(
    threshold_percent: float = Query(10.0, ge=0.0),
) -> List[Dict[str, Any]]:
    """Return districts with significant flood changes."""
    try:
        return satellite_service.get_significant_flood_changes(
            threshold_percent
        )

    except Exception as exc:
        logger.exception("Failed to retrieve significant flood changes")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/district/{district}", response_model=Dict[str, Any])
def get_satellite_analysis_by_district_route(
    district: str,
) -> Dict[str, Any]:
    """Return satellite analysis for a district."""
    try:
        analysis = satellite_service.get_satellite_analysis_by_district(
            district
        )

        if analysis is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Satellite analysis not found for district",
            )

        return analysis

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to retrieve satellite analysis")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc