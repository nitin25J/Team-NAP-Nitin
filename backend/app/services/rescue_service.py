import logging
from typing import Any, Dict, List, Optional
from app.database.loader import load_json

logger = logging.getLogger(__name__)

FILENAME = "rescue.json"


def get_all_rescue_teams() -> List[Dict[str, Any]]:
    """Return all rescue teams from SQLite database."""
    data = load_json(FILENAME)
    if isinstance(data, list):
        return data
    elif isinstance(data, dict):
        return data.get("rescue_teams", [])
    return []


def get_team_by_id(team_id: str) -> Optional[Dict[str, Any]]:
    """Return a single rescue team matching ID."""
    teams = get_all_rescue_teams()
    for team in teams:
        if str(team.get("id")) == str(team_id) or team.get("team_id") == team_id:
            return team
    return None


def get_teams_by_district(district: str) -> List[Dict[str, Any]]:
    """Return rescue teams filtered by district."""
    teams = get_all_rescue_teams()
    return [
        team for team in teams
        if team.get("district", "").lower() == district.lower()
    ]


def get_deployed_teams() -> List[Dict[str, Any]]:
    """Return rescue teams currently deployed."""
    teams = get_all_rescue_teams()
    return [team for team in teams if (team.get("status") or "").lower() == "deployed"]


def get_standby_teams() -> List[Dict[str, Any]]:
    """Return rescue teams currently on standby."""
    teams = get_all_rescue_teams()
    return [team for team in teams if (team.get("status") or "").lower() == "standby"]


def get_teams_by_type(team_type: str) -> List[Dict[str, Any]]:
    """Return rescue teams filtered by organization type."""
    teams = get_all_rescue_teams()
    return [
        team for team in teams
        if team_type.lower() in (team.get("type") or "").lower()
    ]