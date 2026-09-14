"""
Varuna AI — Centralized Application Configuration
Uses Pydantic BaseSettings for environment variable management.
"""

import os
from pathlib import Path
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Application
    APP_NAME: str = "Varuna AI"
    APP_VERSION: str = "2.0.0"
    DEBUG: bool = False

    # Server
    PORT: int = 8000

    # Database
    DATABASE_URL: str = "postgresql://postgres:nitin$11122@localhost/varuna"

    # CORS
    CORS_ORIGINS: str = "*"

    # Weather API
    OPENMETEO_API_URL: str = "https://api.open-meteo.com/v1/forecast"

    # AI / LLM (prepared for future integration)
    AI_PROVIDER: str = "rule-based"  # "rule-based" | "gemini" | "openai"
    GEMINI_API_KEY: str = ""
    OPENAI_API_KEY: str = ""

    # Security
    SECRET_KEY: str = "varuna-dev-secret-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    model_config = {
        "env_file": str(Path(__file__).resolve().parent.parent.parent / ".env"),
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }

    @property
    def cors_origins_list(self) -> list[str]:
        if self.CORS_ORIGINS == "*":
            return ["*"]
        return [o.strip() for o in self.CORS_ORIGINS.split(",")]


@lru_cache()
def get_settings() -> Settings:
    """Cached settings singleton."""
    return Settings()
