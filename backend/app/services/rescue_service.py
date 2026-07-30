import logging
from typing import Any, Dict, List, Optional

from app.database.loader import load_json

logger = logging.getLogger(__name__)

FILENAME = "rescue.json"


def get_all_rescue_teams() -> List[Dict[str, Any]]:
    """Return all rescue teams from the database."""
    data = load_json(FILENAME)
    teams = data.get("rescue_teams", []) if isinstance(data, dict) else []
    return teams


def get_team_by_id(team_id: str) -> Optional[Dict[str, Any]]:
    """Return a single rescue team matching the given ID."""
    teams = get_all_rescue_teams()
    for team in teams:
        if team.get("id") == team_id:
            return team
    logger.warning("Rescue team not found: %s", team_id)
    return None


def get_teams_by_district(district: str) -> List[Dict[str, Any]]:
    """Return rescue teams filtered by district (case-insensitive)."""
    teams = get_all_rescue_teams()
    return [
        team for team in teams
        if team.get("district", "").lower() == district.lower()
    ]


def get_deployed_teams() -> List[Dict[str, Any]]:
    """Return rescue teams currently deployed."""
    teams = get_all_rescue_teams()
    return [team for team in teams if team.get("status") == "Deployed"]


def get_standby_teams() -> List[Dict[str, Any]]:
    """Return rescue teams currently on standby."""
    teams = get_all_rescue_teams()
    return [team for team in teams if team.get("status") == "Standby"]


def get_teams_by_type(team_type: str) -> List[Dict[str, Any]]:
    """Return rescue teams filtered by organization type (e.g. NDRF, SDRF)."""
    teams = get_all_rescue_teams()
    return [
        team for team in teams
        if team.get("type", "").lower() == team_type.lower()
    ]