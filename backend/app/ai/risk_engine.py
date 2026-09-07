# backend/app/ai/risk_engine.py

import logging
from typing import Literal

logger = logging.getLogger(__name__)

RiskLevel = Literal["Low", "Medium", "High", "Severe"]


def calculate_flood_risk(
    rainfall_mm: float,
    river_level_m: float,
    threshold_river_m: float,
    drainage_efficiency: float = 1.0,
) -> RiskLevel:
    """
    Calculates the flood risk level based on rainfall, river water levels,
    and drainage factors.

    Args:
        rainfall_mm (float): Accumulated rainfall in millimeters over 24 hours.
        river_level_m (float): Current river water level in meters.
        threshold_river_m (float): Danger mark/threshold river level in meters.
        drainage_efficiency (float): Factor representing drainage capacity (0.1 to 1.0).

    Returns:
        RiskLevel: "Low", "Medium", "High", or "Severe".
    """
    if rainfall_mm < 0 or river_level_m < 0 or threshold_river_m <= 0:
        logger.error(
            "Invalid input parameters: rainfall=%.2f, river_level=%.2f, threshold=%.2f",
            rainfall_mm,
            river_level_m,
            threshold_river_m,
        )
        raise ValueError(
            "Environmental metric inputs must be non-negative, and threshold must be positive."
        )

    river_ratio = river_level_m / threshold_river_m
    effective_rainfall = rainfall_mm / max(drainage_efficiency, 0.1)

    logger.debug(
        "Calculating flood risk - River Ratio: %.2f, Effective Rainfall: %.2f",
        river_ratio,
        effective_rainfall,
    )

    if river_ratio >= 1.2 or effective_rainfall >= 250.0:
        risk: RiskLevel = "Severe"
    elif river_ratio >= 1.0 or effective_rainfall >= 150.0:
        risk = "High"
    elif river_ratio >= 0.8 or effective_rainfall >= 64.5:
        risk = "Medium"
    else:
        risk = "Low"

    logger.info("Flood risk calculated: %s", risk)
    return risk


def calculate_cyclone_risk(
    sustained_wind_speed_kmh: float,
    pressure_mb: float,
    storm_surge_m: float = 0.0,
) -> RiskLevel:
    """
    Calculates the cyclone risk level based on sustained wind speeds,
    barometric pressure, and predicted storm surge height.

    Args:
        sustained_wind_speed_kmh (float): 3-minute/10-minute sustained wind speed in km/h.
        pressure_mb (float): Central barometric pressure in millibars (hPa).
        storm_surge_m (float): Predicted storm surge height in meters.

    Returns:
        RiskLevel: "Low", "Medium", "High", or "Severe".
    """
    if sustained_wind_speed_kmh < 0 or pressure_mb <= 0 or storm_surge_m < 0:
        logger.error(
            "Invalid input parameters: wind=%.2f, pressure=%.2f, surge=%.2f",
            sustained_wind_speed_kmh,
            pressure_mb,
            storm_surge_m,
        )
        raise ValueError(
            "Atmospheric metric inputs must be non-negative and positive for pressure."
        )

    logger.debug(
        "Calculating cyclone risk - Wind: %.2f km/h, Pressure: %.2f mb, Surge: %.2f m",
        sustained_wind_speed_kmh,
        pressure_mb,
        storm_surge_m,
    )

    if sustained_wind_speed_kmh >= 118 or pressure_mb <= 970 or storm_surge_m >= 3.0:
        risk: RiskLevel = "Severe"
    elif sustained_wind_speed_kmh >= 89 or pressure_mb <= 985 or storm_surge_m >= 1.5:
        risk = "High"
    elif sustained_wind_speed_kmh >= 62 or pressure_mb <= 995 or storm_surge_m >= 0.5:
        risk = "Medium"
    else:
        risk = "Low"

    logger.info("Cyclone risk calculated: %s", risk)
    return risk
