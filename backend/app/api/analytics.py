# backend/app/api/analytics.py

import logging
from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, status

from app.services import analytics_service

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get("/", response_model=Dict[str, Any])
def get_analytics_overview_route() -> Dict[str, Any]:
    """Return the complete analytics dataset."""
    try:
        return analytics_service.get_analytics_overview()
    except Exception as exc:
        logger.exception("Failed to retrieve analytics overview")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/summary", response_model=Dict[str, Any])
def get_summary_route() -> Dict[str, Any]:
    """Return analytics summary."""
    try:
        return analytics_service.get_summary()
    except Exception as exc:
        logger.exception("Failed to retrieve analytics summary")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/district-impact", response_model=List[Dict[str, Any]])
def get_district_wise_impact_route() -> List[Dict[str, Any]]:
    """Return district-wise disaster impact."""
    try:
        return analytics_service.get_district_wise_impact()
    except Exception as exc:
        logger.exception("Failed to retrieve district-wise impact")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/monthly-trend", response_model=List[Dict[str, Any]])
def get_monthly_trend_route() -> List[Dict[str, Any]]:
    """Return monthly disaster trends."""
    try:
        return analytics_service.get_monthly_trend()
    except Exception as exc:
        logger.exception("Failed to retrieve monthly trends")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/disaster-type-distribution", response_model=Dict[str, Any])
def get_disaster_type_distribution_route() -> Dict[str, Any]:
    """Return disaster type distribution."""
    try:
        return analytics_service.get_disaster_type_distribution()
    except Exception as exc:
        logger.exception("Failed to retrieve disaster type distribution")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/district-impact/{district}", response_model=Dict[str, Any])
def get_district_impact_by_name_route(district: str) -> Dict[str, Any]:
    """Return analytics for a specific district."""
    try:
        result = analytics_service.get_district_impact_by_name(district)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="District analytics not found",
            )

        return result

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to retrieve district analytics")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc
