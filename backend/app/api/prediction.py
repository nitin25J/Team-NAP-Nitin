# backend/app/api/prediction.py

import logging
from typing import Any, Dict, List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services import prediction_service

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/prediction",
    tags=["AI Prediction"],
)

@router.get("/", response_model=Dict[str, Any])
def get_prediction_data_route(db: Session = Depends(get_db)) -> Dict[str, Any]:
    try:
        return prediction_service.get_prediction_data(db)
    except Exception as exc:
        logger.exception("Failed to retrieve predictions")
        raise HTTPException(status_code=500, detail="Internal server error") from exc

@router.get("/all", response_model=List[Dict[str, Any]])
def get_all_predictions_route(db: Session = Depends(get_db)) -> List[Dict[str, Any]]:
    try:
        return prediction_service.get_all_predictions(db)
    except Exception as exc:
        logger.exception("Failed to retrieve predictions")
        raise HTTPException(status_code=500, detail="Internal server error") from exc
