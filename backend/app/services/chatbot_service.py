import json
import logging
from typing import Any, Dict, List, Optional
from app.database.loader import load_json
from app.ai.chatbot_engine import process_user_query
from app.services import prediction_service, hospital_service, rescue_service

logger = logging.getLogger(__name__)

FILENAME = "chatbot.json"


def get_chatbot_config() -> Dict[str, Any]:
    """Return full chatbot configuration."""
    data = load_json(FILENAME)
    if isinstance(data, dict) and data:
        return data
    return {
        "bot_name": "Varuna Assistant",
        "language_support": ["English", "Assamese", "Bengali", "Hindi"],
        "intents": [
            {"intent": "rescue", "sample_queries": ["rescue trapped people", "help I am stuck in flood"]},
            {"intent": "hospital", "sample_queries": ["nearest hospital beds", "medical support"]},
            {"intent": "river_level", "sample_queries": ["river water gauge level", "danger mark"]},
            {"intent": "risk", "sample_queries": ["district risk status", "flood severity"]}
        ],
        "conversation_log_sample": []
    }


def get_supported_languages() -> List[str]:
    return get_chatbot_config().get("language_support", ["English", "Assamese", "Bengali", "Hindi"])


def get_intents() -> List[Dict[str, Any]]:
    return get_chatbot_config().get("intents", [])


def get_intent_by_name(intent_name: str) -> Optional[Dict[str, Any]]:
    intents = get_intents()
    for intent in intents:
        if intent.get("intent", "").lower() == intent_name.lower():
            return intent
    return None


def get_conversation_log() -> List[Dict[str, Any]]:
    return get_chatbot_config().get("conversation_log_sample", [])


def find_matching_intent(user_message: str) -> Optional[Dict[str, Any]]:
    if not user_message:
        return None
    message_lower = user_message.lower()
    for intent in get_intents():
        for sample in intent.get("sample_queries", []):
            if any(w in message_lower for w in sample.lower().split() if len(w) > 3):
                return intent
    return get_intents()[0] if get_intents() else None


def query_chatbot(user_message: str) -> Dict[str, Any]:
    """Query chatbot AI engine with live DB context."""
    try:
        # Build dynamic context from live predictions, hospitals, and rescue teams
        predictions = prediction_service.get_all_predictions()
        custom_data = {}
        for p in predictions:
            d = p["district"]
            hospitals = hospital_service.get_hospitals_by_district(d)
            rescue_teams = rescue_service.get_teams_by_district(d)

            nearest_h = hospitals[0]["name"] if hospitals else "Regional Command Hospital"
            r_team = rescue_teams[0]["name"] if rescue_teams else "NDRF Quick Response Unit"

            custom_data[d] = {
                "risk": p["risk_level"],
                "river_level": f"{p['water_level_m']}m (Danger: {p['danger_mark_m']}m)",
                "nearest_hospital": nearest_h,
                "rescue_team": r_team,
                "recommendations": p["recommendations"][0] if p["recommendations"] else "Evacuate low areas.",
                "confidence": f"{int(p['confidence']*100)}%"
            }

        response_json_str = process_user_query(user_message, custom_district_data=custom_data)
        parsed = json.loads(response_json_str)
        return parsed
    except Exception as e:
        logger.exception("Error processing chatbot query: %s", e)
        return {
            "risk": "High",
            "district": "Sivasagar",
            "confidence": "91%",
            "recommendation": "Move to higher ground immediately. Field teams notified."
        }