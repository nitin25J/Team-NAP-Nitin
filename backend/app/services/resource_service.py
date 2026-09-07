import logging
from typing import Any, Dict, List
from app.database.database import SessionLocal
from app.database.db_models import ResourceItemModel, ShelterModel

logger = logging.getLogger(__name__)

FILENAME = "resources.json"


def get_resource_data() -> Dict[str, Any]:
    """Return the full resource dataset."""
    db = SessionLocal()
    try:
        resources = db.query(ResourceItemModel).all()
        shelters = db.query(ShelterModel).all()

        items_list = [r.to_dict() for r in resources]
        shelters_list = [s.to_dict() for s in shelters]

        return {
            "inventory": items_list,
            "inventory_summary": {
                r["name"].lower().replace(" ", "_"): r["have"] for r in items_list
            },
            "shelters": shelters_list,
        }
    finally:
        db.close()


def get_inventory_items() -> List[Dict[str, Any]]:
    """Return all equipment/supply inventory items."""
    db = SessionLocal()
    try:
        resources = db.query(ResourceItemModel).all()
        return [r.to_dict() for r in resources]
    finally:
        db.close()


def get_inventory_summary() -> Dict[str, Any]:
    """Return summary dictionary of total available resources."""
    items = get_inventory_items()
    return {r["name"]: {"available": r["have"], "total": r["total"]} for r in items}


def get_district_resources() -> List[Dict[str, Any]]:
    """Return resource allocation for all districts."""
    db = SessionLocal()
    try:
        shelters = db.query(ShelterModel).all()
        districts_map: Dict[str, List[Dict[str, Any]]] = {}
        for s in shelters:
            d = s.district
            if d not in districts_map:
                districts_map[d] = []
            districts_map[d].append(s.to_dict())

        return [
            {"district": district, "shelters": s_list}
            for district, s_list in districts_map.items()
        ]
    finally:
        db.close()


def get_resources_by_district(district: str) -> Dict[str, Any]:
    """Return resource allocation for a specific district."""
    db = SessionLocal()
    try:
        shelters = (
            db.query(ShelterModel).filter(ShelterModel.district.ilike(district)).all()
        )
        return {"district": district, "shelters": [s.to_dict() for s in shelters]}
    finally:
        db.close()


def get_shelters_by_district(district: str) -> List[Dict[str, Any]]:
    """Return shelters for a district."""
    db = SessionLocal()
    try:
        shelters = (
            db.query(ShelterModel).filter(ShelterModel.district.ilike(district)).all()
        )
        return [s.to_dict() for s in shelters]
    finally:
        db.close()


def get_all_shelters() -> List[Dict[str, Any]]:
    """Return all relief shelters."""
    db = SessionLocal()
    try:
        shelters = db.query(ShelterModel).all()
        return [s.to_dict() for s in shelters]
    finally:
        db.close()
