# backend/app/api/chatbot.py

import logging
from typing import Any, Dict, List

from fastapi import APIRouter, Body, HTTPException, Query, status

from app.services import chatbot_service

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/chatbot",
    tags=["Chatbot"],
)


@router.get("/", response_model=Dict[str, Any])
def get_chatbot_config_route() -> Dict[str, Any]:
    """Return chatbot configuration."""
    try:
        return chatbot_service.get_chatbot_config()
    except Exception as exc:
        logger.exception("Failed to retrieve chatbot configuration")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/languages", response_model=List[str])
def get_supported_languages_route() -> List[str]:
    """Return supported chatbot languages."""
    try:
        return chatbot_service.get_supported_languages()
    except Exception as exc:
        logger.exception("Failed to retrieve supported languages")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/intents", response_model=List[Dict[str, Any]])
def get_intents_route() -> List[Dict[str, Any]]:
    """Return all chatbot intents."""
    try:
        return chatbot_service.get_intents()
    except Exception as exc:
        logger.exception("Failed to retrieve chatbot intents")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/intents/match", response_model=Dict[str, Any])
def find_matching_intent_route(
    user_message: str = Query(..., description="User message to analyze"),
) -> Dict[str, Any]:
    """Find the best matching intent for a user message."""
    try:
        result = chatbot_service.find_matching_intent(user_message)

        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Matching intent not found",
            )

        return result

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to match chatbot intent")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/intents/{intent_name}", response_model=Dict[str, Any])
def get_intent_by_name_route(intent_name: str) -> Dict[str, Any]:
    """Return a chatbot intent by name."""
    try:
        result = chatbot_service.get_intent_by_name(intent_name)

        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Intent not found",
            )

        return result

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to retrieve chatbot intent")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.get("/conversation-log", response_model=List[Dict[str, Any]])
def get_conversation_log_route() -> List[Dict[str, Any]]:
    """Return chatbot conversation log."""
    try:
        return chatbot_service.get_conversation_log()
    except Exception as exc:
        logger.exception("Failed to retrieve conversation log")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc


@router.post("/query", response_model=Dict[str, Any])
def query_chatbot_route(
    payload: Dict[str, Any] = Body(...),
) -> Dict[str, Any]:
    """Process natural language chatbot query."""
    try:
        user_message = payload.get("message") or payload.get("query") or ""
        return chatbot_service.query_chatbot(user_message)
    except Exception as exc:
        logger.exception("Failed to query chatbot")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc