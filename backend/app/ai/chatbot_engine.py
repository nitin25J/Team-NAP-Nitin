# backend/app/ai/chatbot_engine.py

import json
import logging
import re
from typing import Dict, Any, List, Optional, Tuple

logger = logging.getLogger(__name__)


# Standard mock state data used for rule matching context
DEFAULT_DISTRICT_DATA: Dict[str, Any] = {
    "Sivasagar": {
        "risk": "High",
        "river_level": "1.8m above danger mark",
        "nearest_hospital": "Sivasagar Civil Hospital, Joysagar (Distance: 3.2 km)",
        "rescue_team": "NDRF Battalion 12 dispatched to sector 4",
        "recommendations": "Evacuate Wards 4-7 immediately.",
        "confidence": "91%",
    },
    "Cachar": {
        "risk": "Severe",
        "river_level": "2.4m above danger mark",
        "nearest_hospital": "Silchar Medical College & Hospital (Distance: 5.1 km)",
        "rescue_team": "SDRF + Indian Army Column deployed",
        "recommendations": "Move to elevated relief shelters in Zone B.",
        "confidence": "95%",
    },
    "Kamrup": {
        "risk": "Medium",
        "river_level": "0.4m below danger mark",
        "nearest_hospital": "Gauhati Medical College and Hospital (Distance: 2.0 km)",
        "rescue_team": "Local Quick Response Teams on standby",
        "recommendations": "Prepare emergency Go-Bags and avoid riverbanks.",
        "confidence": "88%",
    },
}


def _extract_district(question: str) -> str:
    """Extracts known district name from text or returns default fallback."""
    for district in DEFAULT_DISTRICT_DATA.keys():
        if re.search(r"\b" + re.escape(district) + r"\b", question, re.IGNORECASE):
            return district
    return "Sivasagar"


def _match_intent(question: str) -> str:
    """Determines intent from keywords using precompiled patterns."""
    q_lower = question.lower()

    if any(k in q_lower for k in ["rescue", "trapped", "help", "save", "sos", "stuck"]):
        return "rescue"
    elif any(k in q_lower for k in ["hospital", "medical", "doctor", "clinic", "health"]):
        return "hospital"
    elif any(k in q_lower for k in ["river", "water", "level", "gauge", "flood level"]):
        return "river_level"
    elif any(k in q_lower for k in ["risk", "status", "severity", "danger", "condition"]):
        return "risk"
    else:
        return "general"


def process_user_query(question: str, custom_district_data: Optional[Dict[str, Any]] = None) -> str:
    """
    Processes a user question using deterministic rule matching and returns a structured JSON response string.

    Args:
        question (str): The raw text input query from the user.
        custom_district_data (Optional[Dict[str, Any]]): Optional state database override.

    Returns:
        str: Valid serialized JSON string representing the response payload.
    """
    if not question or not question.strip():
        logger.warning("Received empty or whitespace user query.")
        return json.dumps({
            "error": "Empty question provided.",
            "recommendation": "Please provide a valid query regarding disaster status or assistance.",
        })

    data_store = custom_district_data if custom_district_data is not None else DEFAULT_DISTRICT_DATA

    district = _extract_district(question)
    intent = _match_intent(question)

    district_info = data_store.get(district, data_store["Sivasagar"])

    logger.info("Processing query intent='%s' for district='%s'", intent, district)

    response_payload: Dict[str, Any] = {
        "risk": district_info["risk"],
        "district": district,
        "confidence": district_info["confidence"],
        "recommendation": district_info["recommendations"],
    }

    if intent == "rescue":
        response_payload["action"] = "RESCUE_DISPATCHED"
        response_payload["details"] = district_info["rescue_team"]
        response_payload["recommendation"] = "Move to higher ground immediately. NDRF/SDRF informed."
    elif intent == "hospital":
        response_payload["action"] = "MEDICAL_INFO"
        response_payload["nearest_facility"] = district_info["nearest_hospital"]
    elif intent == "river_level":
        response_payload["action"] = "WATER_LEVEL_METRICS"
        response_payload["river_level"] = district_info["river_level"]
    elif intent == "risk":
        response_payload["action"] = "ASSESS_RISK"

    return json.dumps(response_payload, indent=2)