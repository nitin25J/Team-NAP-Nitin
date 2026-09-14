import logging
from typing import Any, Dict, List
from fastapi import APIRouter, HTTPException, status
from app.services import alert_service

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/alerts",
    tags=["Emergency Alerts"],
)

@router.get("/", response_model=List[Dict[str, Any]])
def get_all_alerts_route() -> List[Dict[str, Any]]:
    return alert_service.get_all_alerts()

@router.get("/active", response_model=List[Dict[str, Any]])
def get_active_alerts_route() -> List[Dict[str, Any]]:
    return alert_service.get_active_alerts()

@router.get("/district/{district}", response_model=List[Dict[str, Any]])
def get_alerts_by_district_route(district: str) -> List[Dict[str, Any]]:
    return alert_service.get_alerts_by_district(district)
