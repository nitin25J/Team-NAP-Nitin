# backend/app/api/reports.py

import logging
from typing import Any, Dict, List

from fastapi import APIRouter, Body, HTTPException, status

from app.services import report_service

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)


@router.get("/", response_model=List[Dict[str, Any]])
def get_all_reports_route() -> List[Dict[str, Any]]:
    """Return all citizen reports."""
    try:
        return report_service.get_all_reports()

    except Exception as exc:
        logger.exception("Failed to retrieve reports")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/district/{district}", response_model=List[Dict[str, Any]])
def get_reports_by_district_route(
    district: str,
) -> List[Dict[str, Any]]:
    """Return reports for a district."""
    try:
        return report_service.get_reports_by_district(district)

    except Exception as exc:
        logger.exception("Failed to retrieve district reports")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/status/{report_status}", response_model=List[Dict[str, Any]])
def get_reports_by_status_route(
    report_status: str,
) -> List[Dict[str, Any]]:
    """Return reports filtered by status."""
    try:
        return report_service.get_reports_by_status(report_status)

    except Exception as exc:
        logger.exception("Failed to retrieve reports by status")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/{report_id}", response_model=Dict[str, Any])
def get_report_by_id_route(
    report_id: str,
) -> Dict[str, Any]:
    """Return a report by ID."""
    try:
        report = report_service.get_report_by_id(report_id)

        if report is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Report not found",
            )

        return report

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to retrieve report")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.post("/", response_model=Dict[str, Any])
def add_report_route(
    new_report: Dict[str, Any] = Body(...),
) -> Dict[str, Any]:
    """Add a new citizen report."""
    try:
        success = report_service.add_report(new_report)

        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to save report",
            )

        return {
            "success": True,
            "message": "Report added successfully",
        }

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to add report")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc
