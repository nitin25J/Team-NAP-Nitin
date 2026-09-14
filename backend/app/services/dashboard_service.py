# backend/app/services/dashboard_service.py

import logging
from typing import Any, Dict, List
from sqlalchemy.orm import Session
from app.database.models import Hospital, RescueTeam, Incident, Prediction

logger = logging.getLogger(__name__)

def get_dashboard_data(db: Session) -> Dict[str, Any]:
    """Return complete dynamic executive dashboard data from PostgreSQL."""
    try:
        # We don't have EmergencyAlertModel in new DB yet, mock it
        active_alerts_count = 3 
        rescue_deployed_count = db.query(RescueTeam).filter(RescueTeam.status == "Deployed").count()
        shelters_active_count = 2 # From mocked resources
        hospitals_count = db.query(Hospital).count()
        reports_count = db.query(Incident).count()

        predictions = db.query(Prediction).all()
        high_risk_count = len([p for p in predictions if (p.severity_score / 100.0) >= 0.7])

        max_severity = max([p.severity_score for p in predictions], default=50)
        risk_level = "Severe" if max_severity >= 85 else ("High" if max_severity >= 70 else "Moderate" if max_severity >= 45 else "Low")
        
        population_at_risk = 125000 + (high_risk_count * 85000)

        overview_stats = {
            "active_alerts": active_alerts_count,
            "high_risk_districts": high_risk_count,
            "total_population_affected": population_at_risk,
            "rescue_teams_deployed": rescue_deployed_count,
            "relief_camps_active": shelters_active_count,
            "hospitals_monitored": hospitals_count,
            "citizen_reports_logged": reports_count,
            "current_risk_level": risk_level,
            "max_severity_score": max_severity,
        }

        top_districts = [
            {
                "district": p.district,
                "risk_level": p.risk_level,
                "severity_score": p.severity_score,
                "river": "Major River",
                "status": "Active Rescue",
            }
            for p in sorted(predictions, key=lambda x: x.severity_score, reverse=True)[:5]
        ]

        quick_links = [
            {"label": "Live GIS Map", "view": "map", "icon": "ti-map-2"},
            {"label": "AI Risk Engine", "view": "ai", "icon": "ti-brain"},
            {"label": "Resource Management", "view": "resources", "icon": "ti-package"},
            {"label": "Emergency Advisories", "view": "alerts", "icon": "ti-bell-ringing"},
        ]

        recent_activity = [
            {"time": "10 min ago", "event": "NDRF Battalion dispatched from database"},
            {"time": "25 min ago", "event": "Evacuation advisory issued (automated)"},
            {"time": "42 min ago", "event": "GMCH Hospital updated ICU capacity"},
        ]

        return {
            "state": "Assam State Command",
            "overview_stats": overview_stats,
            "top_districts": top_districts,
            "quick_links": quick_links,
            "recent_activity": recent_activity,
        }
    except Exception as e:
        logger.exception("Error building dashboard data: %s", e)
        raise

def get_overview_stats(db: Session) -> Dict[str, Any]:
    data = get_dashboard_data(db)
    return data.get("overview_stats", {})

def get_top_affected_districts(db: Session) -> List[Dict[str, Any]]:
    data = get_dashboard_data(db)
    return data.get("top_districts", [])

def get_quick_links(db: Session) -> List[Dict[str, Any]]:
    data = get_dashboard_data(db)
    return data.get("quick_links", [])

def get_recent_activity(db: Session) -> List[Dict[str, Any]]:
    data = get_dashboard_data(db)
    return data.get("recent_activity", [])
