# backend/app/ai/severity_calculator.py

import logging
from typing import Dict, Final

logger = logging.getLogger(__name__)

# Weight definitions for severity score evaluation
WEIGHT_RAINFALL: Final[float] = 0.30
WEIGHT_RIVER: Final[float] = 0.35
WEIGHT_WIND: Final[float] = 0.20
WEIGHT_REPORTS: Final[float] = 0.15

# Baseline reference thresholds for normalization
MAX_RAINFALL_MM: Final[float] = 300.0
MAX_WIND_SPEED_KMH: Final[float] = 180.0
MAX_REPORTS_COUNT: Final[int] = 500


def _normalize_metric(val: float, max_val: float) -> float:
    """Helper function to normalize values to a 0.0 - 1.0 range."""
    return min(max(val / max_val, 0.0), 1.0)


def calculate_severity_score(
    rainfall_mm: float,
    river_level_m: float,
    danger_river_level_m: float,
    wind_speed_kmh: float,
    reports_count: int,
) -> float:
    """
    Calculates a overall composite disaster severity score ranging from 0.0 to 100.0.

    Args:
        rainfall_mm (float): 24-hour accumulated rainfall in mm.
        river_level_m (float): Current river water level in meters.
        danger_river_level_m (float): Designated danger level for the river in meters.
        wind_speed_kmh (float): Maximum wind speed in km/h.
        reports_count (int): Total citizen distress reports/calls logged.

    Returns:
        float: Bounded severity score between 0.0 and 100.0.
    """
    if any(
        param < 0
        for param in (rainfall_mm, river_level_m, wind_speed_kmh, reports_count)
    ):
        logger.error("Negative values detected in severity input parameters.")
        raise ValueError("Metrics inputs must be non-negative.")

    if danger_river_level_m <= 0:
        logger.error("Invalid danger river level provided: %.2f", danger_river_level_m)
        raise ValueError("Danger river level must be greater than zero.")

    # 1. Normalize individual factor components
    norm_rainfall = _normalize_metric(rainfall_mm, MAX_RAINFALL_MM)
    norm_river = _normalize_metric(river_level_m, danger_river_level_m * 1.3)
    norm_wind = _normalize_metric(wind_speed_kmh, MAX_WIND_SPEED_KMH)
    norm_reports = _normalize_metric(float(reports_count), float(MAX_REPORTS_COUNT))

    # 2. Weighted Sum Calculation
    composite_ratio = (
        (norm_rainfall * WEIGHT_RAINFALL)
        + (norm_river * WEIGHT_RIVER)
        + (norm_wind * WEIGHT_WIND)
        + (norm_reports * WEIGHT_REPORTS)
    )

    # 3. Scale to 0-100 range and cap
    raw_score = composite_ratio * 100.0
    final_score = round(min(max(raw_score, 0.0), 100.0), 2)

    logger.info(
        "Calculated disaster severity score: %.2f (Rainfall: %.1f, River: %.2f/%.2f, Wind: %.1f, Reports: %d)",
        final_score,
        rainfall_mm,
        river_level_m,
        danger_river_level_m,
        wind_speed_kmh,
        reports_count,
    )

    return final_score
