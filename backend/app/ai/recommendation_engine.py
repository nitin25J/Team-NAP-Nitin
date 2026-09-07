# backend/app/ai/recommendation_engine.py

import logging
from typing import List

logger = logging.getLogger(__name__)


def generate_recommendations(severity_score: float) -> List[str]:
    """
    Generates operational disaster response actions based on the computed severity score.

    Args:
        severity_score (float): A calculated score ranging between 0.0 and 100.0.

    Returns:
        List[str]: Actionable emergency recommendations ordered by priority.
    """
    if not (0.0 <= severity_score <= 100.0):
        logger.error("Severity score out of valid range (0-100): %.2f", severity_score)
        raise ValueError("Severity score must be between 0.0 and 100.0.")

    recommendations: List[str] = []

    if severity_score >= 85.0:
        recommendations.extend(
            [
                "Issue Emergency Alert",
                "Evacuate Area",
                "Deploy NDRF",
                "Deploy Rescue Boats",
                "Open Relief Camps",
                "Increase Medical Support",
            ]
        )
    elif severity_score >= 65.0:
        recommendations.extend(
            [
                "Issue Emergency Alert",
                "Evacuate Area",
                "Deploy Rescue Boats",
                "Open Relief Camps",
                "Increase Medical Support",
            ]
        )
    elif severity_score >= 45.0:
        recommendations.extend(
            [
                "Issue Emergency Alert",
                "Open Relief Camps",
                "Increase Medical Support",
                "Deploy SDRF Local Teams",
            ]
        )
    elif severity_score >= 25.0:
        recommendations.extend(
            [
                "Issue Public Safety Advisory",
                "Monitor River Levels and Weather Updates",
                "Keep Emergency Services on Standby",
            ]
        )
    else:
        recommendations.extend(
            [
                "Continue Normal Monitoring",
                "Maintain Standard Emergency Preparedness",
            ]
        )

    logger.info(
        "Generated %d recommendations for severity score: %.2f",
        len(recommendations),
        severity_score,
    )
    return recommendations
