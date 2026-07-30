# backend/app/api/prediction.py

import logging
from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, Query, status

from app.services import prediction_service

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"],
)


@router.get("/", response_model=Dict[str, Any])
def get_prediction_data_route() -> Dict[str, Any]:
    """Return complete prediction dataset."""
    try:
        result = prediction_service.get_prediction_data()

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Prediction data not found",
            )

        return result

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to retrieve prediction data")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/model-info", response_model=Dict[str, Any])
def get_model_info_route() -> Dict[str, Any]:
    """Return AI model information."""
    try:
        return prediction_service.get_model_info()

    except Exception as exc:
        logger.exception("Failed to retrieve model information")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/all", response_model=List[Dict[str, Any]])
def get_all_predictions_route() -> List[Dict[str, Any]]:
    """Return all district predictions."""
    try:
        return prediction_service.get_all_predictions()

    except Exception as exc:
        logger.exception("Failed to retrieve predictions")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/high-risk", response_model=List[Dict[str, Any]])
def get_high_risk_districts_route(
    threshold: float = Query(0.7, ge=0.0, le=1.0),
) -> List[Dict[str, Any]]:
    """Return districts above the specified risk threshold."""
    try:
        return prediction_service.get_high_risk_districts(threshold)

    except Exception as exc:
        logger.exception("Failed to retrieve high-risk districts")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/district/{district}", response_model=Dict[str, Any])
def get_prediction_by_district_route(
    district: str,
) -> Dict[str, Any]:
    """Return prediction for a specific district."""
    try:
        prediction = prediction_service.get_prediction_by_district(district)

        if prediction is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Prediction not found for district",
            )

        return prediction

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to retrieve district prediction")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc