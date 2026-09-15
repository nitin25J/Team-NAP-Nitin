# backend/app/api/rescue.py

import logging
from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, status

from app.services import rescue_service

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/rescue",
    tags=["Rescue"],
)


@router.get("/", response_model=List[Dict[str, Any]])
def get_all_rescue_teams_route() -> List[Dict[str, Any]]:
    """Return all rescue teams."""
    try:
        return rescue_service.get_all_rescue_teams()

    except Exception as exc:
        logger.exception("Failed to retrieve rescue teams")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/deployed", response_model=List[Dict[str, Any]])
def get_deployed_teams_route() -> List[Dict[str, Any]]:
    """Return deployed rescue teams."""
    try:
        return rescue_service.get_deployed_teams()

    except Exception as exc:
        logger.exception("Failed to retrieve deployed rescue teams")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/standby", response_model=List[Dict[str, Any]])
def get_standby_teams_route() -> List[Dict[str, Any]]:
    """Return standby rescue teams."""
    try:
        return rescue_service.get_standby_teams()

    except Exception as exc:
        logger.exception("Failed to retrieve standby rescue teams")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/district/{district}", response_model=List[Dict[str, Any]])
def get_teams_by_district_route(
    district: str,
) -> List[Dict[str, Any]]:
    """Return rescue teams for a district."""
    try:
        return rescue_service.get_teams_by_district(district)

    except Exception as exc:
        logger.exception("Failed to retrieve district rescue teams")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/type/{team_type}", response_model=List[Dict[str, Any]])
def get_teams_by_type_route(
    team_type: str,
) -> List[Dict[str, Any]]:
    """Return rescue teams by organization type."""
    try:
        return rescue_service.get_teams_by_type(team_type)

    except Exception as exc:
        logger.exception("Failed to retrieve rescue teams by type")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/{team_id}", response_model=Dict[str, Any])
def get_team_by_id_route(
    team_id: str,
) -> Dict[str, Any]:
    """Return a rescue team by ID."""
    try:
        team = rescue_service.get_team_by_id(team_id)

        if team is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Rescue team not found",
            )

        return team

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to retrieve rescue team")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc
