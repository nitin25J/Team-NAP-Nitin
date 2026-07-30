import logging
from typing import Any, Dict, List, Optional

from app.database.loader import load_json

logger = logging.getLogger(__name__)

FILENAME = "prediction.json"


def get_prediction_data() -> Dict[str, Any]:
    """Return the full AI prediction dataset."""
    data = load_json(FILENAME)
    if not isinstance(data, dict):
        logger.warning("Prediction data malformed or empty")
        return {}
    return data


def get_model_info() -> Dict[str, Any]:
    """Return model metadata (name, version, last run time)."""
    data = get_prediction_data()
    return {
        "model_name": data.get("model_name"),
        "model_version": data.get("model_version"),
        "last_run": data.get("last_run"),
    }


def get_all_predictions() -> List[Dict[str, Any]]:
    """Return all district-level risk predictions."""
    data = get_prediction_data()
    return data.get("predictions", [])


def get_prediction_by_district(district: str) -> Optional[Dict[str, Any]]:
    """Return the prediction for a specific district."""
    predictions = get_all_predictions()
    for prediction in predictions:
        if prediction.get("district", "").lower() == district.lower():
            return prediction
    logger.warning("Prediction not found for district: %s", district)
    return None


def get_high_risk_districts(threshold: float = 0.7) -> List[Dict[str, Any]]:
    """Return predictions where risk_score meets or exceeds the given threshold."""
    predictions = get_all_predictions()
    return [
        p for p in predictions
        if isinstance(p.get("risk_score"), (int, float)) and p["risk_score"] >= threshold
    ]