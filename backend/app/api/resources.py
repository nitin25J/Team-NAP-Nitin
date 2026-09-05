# backend/app/api/resources.py

import logging
from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, status

from app.services import resource_service

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/resources",
    tags=["Resources"],
)


@router.get("/", response_model=Dict[str, Any])
def get_resource_data_route() -> Dict[str, Any]:
    """Return the complete resource dataset."""
    try:
        result = resource_service.get_resource_data()

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resource data not found",
            )

        return result

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to retrieve resource data")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/summary", response_model=Dict[str, Any])
def get_inventory_summary_route() -> Dict[str, Any]:
    """Return inventory summary."""
    try:
        return resource_service.get_inventory_summary()

    except Exception as exc:
        logger.exception("Failed to retrieve inventory summary")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/items", response_model=List[Dict[str, Any]])
def get_inventory_items_route() -> List[Dict[str, Any]]:
    """Return live equipment/supply inventory list."""
    try:
        return resource_service.get_inventory_items()

    except Exception as exc:
        logger.exception("Failed to retrieve inventory items")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/districts", response_model=List[Dict[str, Any]])
def get_district_resources_route() -> List[Dict[str, Any]]:
    """Return resource allocation for all districts."""
    try:
        return resource_service.get_district_resources()

    except Exception as exc:
        logger.exception("Failed to retrieve district resources")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/shelters", response_model=List[Dict[str, Any]])
def get_all_shelters_route() -> List[Dict[str, Any]]:
    """Return all shelters."""
    try:
        return resource_service.get_all_shelters()

    except Exception as exc:
        logger.exception("Failed to retrieve shelters")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/district/{district}", response_model=Dict[str, Any])
def get_resources_by_district_route(
    district: str,
) -> Dict[str, Any]:
    """Return resources for a district."""
    try:
        resources = resource_service.get_resources_by_district(district)

        if not resources:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resources not found for district",
            )

        return resources

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to retrieve district resources")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/district/{district}/shelters", response_model=List[Dict[str, Any]])
def get_shelters_by_district_route(
    district: str,
) -> List[Dict[str, Any]]:
    """Return shelters for a district."""
    try:
        return resource_service.get_shelters_by_district(district)

    except Exception as exc:
        logger.exception("Failed to retrieve district shelters")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc