# backend/app/api/dashboard.py

import logging
from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, status

from app.services import dashboard_service

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get("/", response_model=Dict[str, Any])
def get_dashboard_data_route() -> Dict[str, Any]:
    """Return complete dashboard data."""
    try:
        return dashboard_service.get_dashboard_data()
    except Exception as exc:
        logger.exception("Failed to retrieve dashboard data")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/overview", response_model=Dict[str, Any])
def get_overview_stats_route() -> Dict[str, Any]:
    """Return dashboard overview statistics."""
    try:
        return dashboard_service.get_overview_stats()
    except Exception as exc:
        logger.exception("Failed to retrieve overview statistics")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/top-districts", response_model=List[Dict[str, Any]])
def get_top_affected_districts_route() -> List[Dict[str, Any]]:
    """Return top affected districts."""
    try:
        return dashboard_service.get_top_affected_districts()
    except Exception as exc:
        logger.exception("Failed to retrieve top affected districts")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/quick-links", response_model=List[Dict[str, Any]])
def get_quick_links_route() -> List[Dict[str, Any]]:
    """Return dashboard quick links."""
    try:
        return dashboard_service.get_quick_links()
    except Exception as exc:
        logger.exception("Failed to retrieve quick links")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/recent-activity", response_model=List[Dict[str, Any]])
def get_recent_activity_route() -> List[Dict[str, Any]]:
    """Return recent dashboard activity."""
    try:
        return dashboard_service.get_recent_activity()
    except Exception as exc:
        logger.exception("Failed to retrieve recent activity")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc
