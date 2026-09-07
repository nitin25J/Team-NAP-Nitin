import logging
from typing import Any, Dict, Optional

from app.database.loader import load_json, save_json

logger = logging.getLogger(__name__)

SETTINGS_FILE = "settings.json"

DEFAULT_SETTINGS: Dict[str, Any] = {
    "app_name": "Varuna AI",
    "theme": "dark",
    "notifications_enabled": True,
    "max_concurrent_tasks": 5,
    "language": "en",
    "auto_save": True,
}


def get_settings() -> Dict[str, Any]:
    """Retrieve application settings from the data loader.

    Returns default settings if data is missing, corrupted, or invalid.
    """
    try:
        data = load_json(SETTINGS_FILE)

        if data is None:
            logger.warning(
                "Settings file '%s' not found or empty. Falling back to default settings.",
                SETTINGS_FILE,
            )
            return DEFAULT_SETTINGS.copy()

        if not isinstance(data, dict):
            logger.error(
                "Invalid settings format in '%s'. Expected dict, got %s. Returning defaults.",
                SETTINGS_FILE,
                type(data).__name__,
            )
            return DEFAULT_SETTINGS.copy()

        # Merge defaults with loaded data to ensure all keys exist
        merged_settings = DEFAULT_SETTINGS.copy()
        merged_settings.update(data)
        return merged_settings

    except Exception as exc:
        logger.exception(
            "Unexpected error while loading settings from '%s': %s",
            SETTINGS_FILE,
            exc,
        )
        return DEFAULT_SETTINGS.copy()


def get_setting(key: str, default: Optional[Any] = None) -> Any:
    """Retrieve a specific setting value by key.

    Args:
        key: The key of the setting to retrieve.
        default: Fallback value if the key does not exist.

    Returns:
        The setting value or the default fallback.
    """
    settings = get_settings()
    return settings.get(key, default)


def update_settings(settings: dict) -> Dict[str, Any]:
    """Update settings with new key-value pairs and persist changes.

    Args:
        settings: Dictionary containing setting updates.

    Returns:
        Dict[str, Any]: The complete updated settings object.
    """
    if not isinstance(settings, dict):
        logger.error(
            "Invalid argument for update_settings. Expected dict, got %s.",
            type(settings).__name__,
        )
        return get_settings()

    if not settings:
        logger.info("Empty dictionary passed to update_settings. No changes made.")
        return get_settings()

    current_settings = get_settings()
    current_settings.update(settings)

    try:
        save_json(SETTINGS_FILE, current_settings)
        logger.info("Successfully updated settings in '%s'.", SETTINGS_FILE)
    except Exception as exc:
        logger.exception(
            "Failed to save updated settings to '%s': %s",
            SETTINGS_FILE,
            exc,
        )

    return current_settings


def update_setting(key: str, value: Any) -> Dict[str, Any]:
    """Convenience function to update a single setting key-value pair.

    Args:
        key: The setting key to set or update.
        value: The value to assign to the setting.

    Returns:
        Dict[str, Any]: The complete updated settings object.
    """
    return update_settings({key: value})


def reset_settings() -> Dict[str, Any]:
    """Reset application settings to default values.

    Returns:
        Dict[str, Any]: The reset default settings object.
    """
    logger.info("Resetting application settings to defaults.")
    try:
        save_json(SETTINGS_FILE, DEFAULT_SETTINGS)
    except Exception as exc:
        logger.exception(
            "Failed to persist default settings to '%s': %s", SETTINGS_FILE, exc
        )

    return DEFAULT_SETTINGS.copy()
