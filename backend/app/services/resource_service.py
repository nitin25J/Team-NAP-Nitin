# backend/app/services/resource_service.py

from typing import Any, Dict, List, Optional
from sqlalchemy.orm import Session
from app.database.models import Resource

def get_resources_data(db: Session) -> Dict[str, Any]:
    resources = db.query(Resource).all()
    
    inventory = []
    for r in resources:
        inventory.append({
            "id": str(r.id),
            "name": r.name,
            "category": r.type,
            "total_quantity": r.total_quantity,
            "available_quantity": r.available_quantity,
            "unit": "Units",
            "last_updated": "Just now",
        })

    # Since shelters are not in the new DB models, we return a mock array here,
    # or you could map Hospitals to shelters. For now we will return some static shelter mock data
    # so the UI does not break.
    shelters = [
        {"id": "1", "name": "Guwahati Relief Camp", "district": "Kamrup", "capacity": 500, "occupancy": 350, "status": "Active"},
        {"id": "2", "name": "Majuli High School", "district": "Majuli", "capacity": 200, "occupancy": 195, "status": "Critical"},
    ]

    return {
        "inventory": inventory,
        "shelters": shelters,
    }
