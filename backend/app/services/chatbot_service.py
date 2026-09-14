import json
import logging
from typing import Any, Dict, List, Optional
import google.generativeai as genai

from app.core.config import get_settings
from app.ai import chatbot_engine

logger = logging.getLogger(__name__)
config = get_settings()

_conversation_log: List[Dict[str, Any]] = []

def get_chatbot_config() -> Dict[str, Any]:
    return {
        "provider": config.AI_PROVIDER,
        "version": "2.0.0",
        "status": "online"
    }

def get_supported_languages() -> List[str]:
    return ["en", "hi", "as", "bn"]

def get_intents() -> List[Dict[str, Any]]:
    return [
        {"name": "rescue", "description": "Request rescue operations"},
        {"name": "hospital", "description": "Find nearby medical facilities"},
        {"name": "river_level", "description": "Check flood water levels"},
        {"name": "risk", "description": "Assess disaster risk"},
        {"name": "general", "description": "General inquiries"}
    ]

def find_matching_intent(user_message: str) -> Optional[Dict[str, Any]]:
    intent = chatbot_engine._match_intent(user_message)
    intents = get_intents()
    for i in intents:
        if i["name"] == intent:
            return i
    return {"name": "general", "description": "General inquiries"}

def get_intent_by_name(intent_name: str) -> Optional[Dict[str, Any]]:
    intents = get_intents()
    for i in intents:
        if i["name"].lower() == intent_name.lower():
            return i
    return None

def get_conversation_log() -> List[Dict[str, Any]]:
    return _conversation_log

def query_chatbot(user_message: str) -> Dict[str, Any]:
    """Process natural language chatbot query."""
    logger.info(f"Querying chatbot with: {user_message}")
    
    response_payload = {}
    
    if config.AI_PROVIDER == "gemini" and config.GEMINI_API_KEY:
        try:
            genai.configure(api_key=config.GEMINI_API_KEY)
            model = genai.GenerativeModel('gemini-pro')
            prompt = f"You are Varuna AI, a disaster intelligence assistant. Help the user with this request: {user_message}"
            response = model.generate_content(prompt)
            
            response_payload = {
                "reply": response.text,
                "provider": "gemini",
                "action": "GENERAL_RESPONSE"
            }
        except Exception as e:
            logger.error(f"Gemini AI failed: {e}. Falling back to rule-based.")
            response_payload = json.loads(chatbot_engine.process_user_query(user_message))
    else:
        # Rule-based fallback
        result_json = chatbot_engine.process_user_query(user_message)
        try:
            parsed = json.loads(result_json)
            reply_text = parsed.get("recommendation", "I have received your request.")
            if "error" in parsed:
                reply_text = parsed["error"]
                
            response_payload = {
                "reply": reply_text,
                "provider": "rule-based",
                "data": parsed
            }
        except:
            response_payload = {
                "reply": result_json,
                "provider": "rule-based"
            }
            
    # Keep log small
    if len(_conversation_log) > 100:
        _conversation_log.pop(0)
    _conversation_log.append({"user": user_message, "bot": response_payload})
    
    return response_payload
