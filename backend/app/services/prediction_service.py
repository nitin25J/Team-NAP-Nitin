# backend/app/services/prediction_service.py

from typing import Any, Dict, List, Optional
from sqlalchemy.orm import Session
from app.database.models import Prediction
from datetime import datetime

def get_all_predictions(db: Session) -> List[Dict[str, Any]]:
    predictions = db.query(Prediction).all()
    return [
        {
            "id": p.id,
            "district": p.district,
            "risk_level": p.risk_level,
            "risk_score": round(p.severity_score / 100.0, 2), # normalized
            "severity_score": p.severity_score,
            "confidence": p.confidence,
            "river_name": "Major River", # mocked since it's not in db yet
            "water_level_m": p.water_level_m,
            "danger_mark_m": p.danger_mark_m,
            "rainfall_mm_24h": p.rainfall_mm_24h,
            "wind_speed_kmh": 15.0, # mocked
            "recommendations": p.recommendations,
            "last_updated": p.timestamp.isoformat() if p.timestamp else datetime.utcnow().isoformat(),
        }
        for p in predictions
    ]

def get_prediction_data(db: Session) -> Dict[str, Any]:
    preds = get_all_predictions(db)
    return {
        "model_name": "Varuna Hydro-Met Neural Risk Fusion v2.4 (DB Backed)",
        "model_version": "2.4.0-Live",
        "last_run": datetime.utcnow().isoformat(),
        "predictions": preds,
    }

def get_prediction_by_district(db: Session, district: str) -> Optional[Dict[str, Any]]:
    preds = get_all_predictions(db)
    for p in preds:
        if p.get("district", "").lower() == district.lower():
            return p
    return None

def get_high_risk_districts(db: Session, threshold: float = 0.7) -> List[Dict[str, Any]]:
    preds = get_all_predictions(db)
    return [p for p in preds if p.get("risk_score", 0) >= threshold]
