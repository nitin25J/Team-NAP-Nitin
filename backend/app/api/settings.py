# backend/app/api/settings.py

import logging
from typing import Any, Dict

from fastapi import APIRouter, Body, HTTPException, status

from app.services import settings_service

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/settings",
    tags=["Settings"],
)


@router.get("/", response_model=Dict[str, Any])
def get_settings_route() -> Dict[str, Any]:
    """Return all application settings."""
    try:
        return settings_service.get_settings()

    except Exception as exc:
        logger.exception("Failed to retrieve settings")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/{key}", response_model=Dict[str, Any])
def get_setting_route(
    key: str,
) -> Dict[str, Any]:
    """Return a specific setting."""
    try:
        value = settings_service.get_setting(key)

        if value is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Setting '{key}' not found",
            )

        return {key: value}

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to retrieve setting")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.put("/", response_model=Dict[str, Any])
def update_settings_route(
    settings: Dict[str, Any] = Body(...),
) -> Dict[str, Any]:
    """Update multiple settings."""
    try:
        return settings_service.update_settings(settings)

    except Exception as exc:
        logger.exception("Failed to update settings")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.put("/{key}", response_model=Dict[str, Any])
def update_setting_route(
    key: str,
    value: Any = Body(...),
) -> Dict[str, Any]:
    """Update a single setting."""
    try:
        return settings_service.update_setting(key, value)

    except Exception as exc:
        logger.exception("Failed to update setting")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.post("/reset", response_model=Dict[str, Any])
def reset_settings_route() -> Dict[str, Any]:
    """Reset settings to default values."""
    try:
        return settings_service.reset_settings()

    except Exception as exc:
        logger.exception("Failed to reset settings")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc
