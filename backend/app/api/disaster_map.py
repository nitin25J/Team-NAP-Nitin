# backend/app/api/disaster_map.py

import logging
from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, status

from app.services import map_service

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/map",
    tags=["Disaster Map"],
)


@router.get("/", response_model=Dict[str, Any])
def get_map_data_route() -> Dict[str, Any]:
    """Return complete map dataset."""
    try:
        result = map_service.get_map_data()

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Map data not found",
            )

        return result

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to retrieve map data")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/center", response_model=Dict[str, Any])
def get_map_center_route() -> Dict[str, Any]:
    """Return default map center."""
    try:
        result = map_service.get_map_center()

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Map center not found",
            )

        return result

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to retrieve map center")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/flood-zones", response_model=List[Dict[str, Any]])
def get_flood_zones_route() -> List[Dict[str, Any]]:
    """Return all flood zones."""
    try:
        return map_service.get_flood_zones()
    except Exception as exc:
        logger.exception("Failed to retrieve flood zones")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/flood-zones/{district}", response_model=Dict[str, Any])
def get_flood_zone_by_district_route(
    district: str,
) -> Dict[str, Any]:
    """Return flood zone for a district."""
    try:
        result = map_service.get_flood_zone_by_district(district)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Flood zone not found for district",
            )

        return result

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to retrieve flood zone")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/rivers", response_model=List[Dict[str, Any]])
def get_river_markers_route() -> List[Dict[str, Any]]:
    """Return river markers."""
    try:
        return map_service.get_river_markers()
    except Exception as exc:
        logger.exception("Failed to retrieve river markers")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/rivers/above-danger", response_model=List[Dict[str, Any]])
def get_rivers_above_danger_level_route() -> List[Dict[str, Any]]:
    """Return rivers above danger level."""
    try:
        return map_service.get_rivers_above_danger_level()
    except Exception as exc:
        logger.exception("Failed to retrieve rivers above danger level")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc