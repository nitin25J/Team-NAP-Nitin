# backend/app/api/resources.py

import logging
from typing import Any, Dict
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services import resource_service

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/resources",
    tags=["Resources"],
)

@router.get("/", response_model=Dict[str, Any])
def get_resources_route(db: Session = Depends(get_db)) -> Dict[str, Any]:
    try:
        return resource_service.get_resources_data(db)
    except Exception as exc:
        logger.exception("Failed to retrieve resources data")
        raise HTTPException(status_code=500, detail="Internal server error") from exc
