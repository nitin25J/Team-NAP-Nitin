from typing import Any, Dict
from pydantic import BaseModel

class SettingsUpdate(BaseModel):
    theme: str
    notifications_enabled: bool
    refresh_rate: int

def get_settings() -> Dict[str, Any]:
    return {
        "theme": "dark",
        "notifications_enabled": True,
        "refresh_rate": 30
    }

def update_settings(settings_data: Dict[str, Any]) -> Dict[str, Any]:
    return settings_data
