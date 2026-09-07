# weather.py
import logging
from typing import Any, Dict, List
from fastapi import APIRouter, HTTPException

from app.services import weather_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/weather", tags=["weather"])


@router.get("/", response_model=Dict[str, Any])
def get_weather_data_route() -> Dict[str, Any]:
    try:
        result = weather_service.get_weather_data()
        if not result:
            raise HTTPException(status_code=404, detail="Weather data not found")
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in get_weather_data_route: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/forecasts", response_model=List[Dict[str, Any]])
def get_district_forecasts_route() -> List[Dict[str, Any]]:
    try:
        return weather_service.get_district_forecasts()
    except Exception as e:
        logger.error(f"Unexpected error in get_district_forecasts_route: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/heavy-rain", response_model=List[Dict[str, Any]])
def get_districts_with_heavy_rain_route() -> List[Dict[str, Any]]:
    try:
        return weather_service.get_districts_with_heavy_rain()
    except Exception as e:
        logger.error(f"Unexpected error in get_districts_with_heavy_rain_route: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/highest-rainfall", response_model=Dict[str, Any])
def get_highest_rainfall_district_route() -> Dict[str, Any]:
    try:
        result = weather_service.get_highest_rainfall_district()
        if result is None:
            raise HTTPException(
                status_code=404, detail="Highest rainfall district not found"
            )
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in get_highest_rainfall_district_route: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/district/{district}", response_model=Dict[str, Any])
def get_forecast_by_district_route(district: str) -> Dict[str, Any]:
    try:
        result = weather_service.get_forecast_by_district(district)
        if result is None:
            raise HTTPException(
                status_code=404, detail="Forecast not found for district"
            )
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in get_forecast_by_district_route: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
