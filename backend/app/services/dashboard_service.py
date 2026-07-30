# backend/app/api/alerts.py

import logging
from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, status

from app.services import alert_service

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"],
)


@router.get("/", response_model=List[Dict[str, Any]])
def get_all_alerts_route() -> List[Dict[str, Any]]:
    """Return all alerts."""
    try:
        return alert_service.get_all_alerts()
    except Exception as exc:
        logger.exception("Failed to retrieve all alerts")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/active", response_model=List[Dict[str, Any]])
def get_active_alerts_route() -> List[Dict[str, Any]]:
    """Return all active alerts."""
    try:
        return alert_service.get_active_alerts()
    except Exception as exc:
        logger.exception("Failed to retrieve active alerts")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/district/{district}", response_model=List[Dict[str, Any]])
def get_alerts_by_district_route(district: str) -> List[Dict[str, Any]]:
    """Return alerts filtered by district."""
    try:
        return alert_service.get_alerts_by_district(district)
    except Exception as exc:
        logger.exception("Failed to retrieve district alerts")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/severity/{severity}", response_model=List[Dict[str, Any]])
def get_alerts_by_severity_route(severity: str) -> List[Dict[str, Any]]:
    """Return alerts filtered by severity."""
    try:
        return alert_service.get_alerts_by_severity(severity)
    except Exception as exc:
        logger.exception("Failed to retrieve severity alerts")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/{alert_id}", response_model=Dict[str, Any])
def get_alert_by_id_route(alert_id: str) -> Dict[str, Any]:
    """Return a single alert by ID."""
    try:
        alert = alert_service.get_alert_by_id(alert_id)

        if alert is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Alert not found",
            )

        return alert

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to retrieve alert")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc