# backend/app/api/alerts.py

import logging
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Body, HTTPException, Query, status

from app.services import alert_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/alerts", tags=["Alerts"])



@router.get("/", response_model=List[Dict[str, Any]])
def get_alerts(
    district: Optional[str] = Query(None),
    severity: Optional[str] = Query(None),
) -> List[Dict[str, Any]]:
    try:
        if district:
            return alert_service.get_alerts_by_district(district)

        if severity:
            return alert_service.get_alerts_by_severity(severity)

        return alert_service.get_active_alerts()

    except Exception as exc:
        logger.exception("Failed to retrieve alerts")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving alerts.",
        ) from exc


@router.get("/{alert_id}", response_model=Dict[str, Any])
def get_alert(alert_id: str) -> Dict[str, Any]:
    try:
        alert = alert_service.get_alert_by_id(alert_id)

        if alert is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Alert '{alert_id}' not found.",
            )

        return alert

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to retrieve alert")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        ) from exc


@router.post("/", response_model=Dict[str, Any])
def create_alert_route(
    alert_payload: Dict[str, Any] = Body(...),
) -> Dict[str, Any]:
    """Issue a new emergency alert."""
    try:
        new_alert = alert_service.create_alert(alert_payload)
        return {
            "success": True,
            "message": "Emergency alert issued successfully",
            "alert": new_alert
        }
    except Exception as exc:
        logger.exception("Failed to issue alert")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        ) from exc