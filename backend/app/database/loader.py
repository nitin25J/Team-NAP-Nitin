import json
import logging
from pathlib import Path
from typing import Any, List, Union

logger = logging.getLogger(__name__)

DATABASE_DIR = Path(__file__).resolve().parent / "dummy"


def load_json(filename: str) -> Union[List[Any], dict]:
    """
    Load JSON data from a file inside the dummy database directory.

    Returns:
        The parsed JSON data (list or dict) on success.
        An empty list ([]) if the file is missing, unreadable, or invalid.
    """
    file_path = DATABASE_DIR / filename

    try:
        with file_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    except FileNotFoundError:
        logger.warning("File not found: %s", file_path)
        return []

    except PermissionError:
        logger.error("Permission denied while reading file: %s", file_path)
        return []

    except json.JSONDecodeError as e:
        logger.error("Invalid JSON in file %s: %s", file_path, e)
        return []

    except Exception as e:
        logger.exception("Unexpected error while loading file %s: %s", file_path, e)
        return []


def save_json(filename: str, data: Any) -> bool:
    """
    Save JSON data to a file inside the dummy database directory.

    Returns:
        True if the save was successful, False otherwise.
    """
    file_path = DATABASE_DIR / filename

    try:
        DATABASE_DIR.mkdir(parents=True, exist_ok=True)

        with file_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return True

    except PermissionError:
        logger.error("Permission denied while writing file: %s", file_path)
        return False

    except TypeError as e:
        logger.error("Data is not JSON serializable for file %s: %s", file_path, e)
        return False

    except Exception as e:
        logger.exception("Unexpected error while saving file %s: %s", file_path, e)
        return False