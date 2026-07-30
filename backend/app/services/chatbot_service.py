import logging
from typing import Any, Dict, List, Optional

from app.database.loader import load_json

logger = logging.getLogger(__name__)

FILENAME = "chatbot.json"


def get_chatbot_config() -> Dict[str, Any]:
    """Return the full chatbot configuration data."""
    data = load_json(FILENAME)
    if not isinstance(data, dict):
        logger.warning("Chatbot data malformed or empty")
        return {}
    return data


def get_supported_languages() -> List[str]:
    """Return list of supported languages."""
    data = get_chatbot_config()
    return data.get("language_support", [])


def get_intents() -> List[Dict[str, Any]]:
    """Return all defined chatbot intents."""
    data = get_chatbot_config()
    return data.get("intents", [])


def get_intent_by_name(intent_name: str) -> Optional[Dict[str, Any]]:
    """Return a specific intent definition by its name."""
    intents = get_intents()
    for intent in intents:
        if intent.get("intent", "").lower() == intent_name.lower():
            return intent
    logger.warning("Intent not found: %s", intent_name)
    return None


def get_conversation_log() -> List[Dict[str, Any]]:
    """Return sample conversation log entries."""
    data = get_chatbot_config()
    return data.get("conversation_log_sample", [])


def find_matching_intent(user_message: str) -> Optional[Dict[str, Any]]:
    """
    Naively match a user message against sample queries within intents.
    Returns the first intent whose sample query shares a keyword with the message.
    """
    if not user_message:
        return None

    message_lower = user_message.lower()
    intents = get_intents()

    for intent in intents:
        for sample in intent.get("sample_queries", []):
            sample_words = set(sample.lower().split())
            message_words = set(message_lower.split())
            if sample_words & message_words:
                return intent

    logger.info("No matching intent found for message: %s", user_message)
    return None