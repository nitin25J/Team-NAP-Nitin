from typing import Any, Dict

def get_satellite_imagery() -> Dict[str, Any]:
    return {
        "images": [],
        "metadata": {"source": "ISRO", "resolution": "10m"}
    }
