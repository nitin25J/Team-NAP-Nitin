from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Text
from app.database.database import Base

class HospitalModel(Base):
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    district = Column(String, index=True)
    beds_available = Column(Integer, default=0)
    beds_total = Column(Integer, default=100)
    icu_available = Column(Integer, default=0)
    icu_total = Column(Integer, default=20)
    lat = Column(Float)
    lng = Column(Float)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "district": self.district,
            "beds_available": self.beds_available,
            "beds_total": self.beds_total,
            "icu_available": self.icu_available,
            "icu_total": self.icu_total,
            "coordinates": {"lat": self.lat, "lng": self.lng} if self.lat and self.lng else None
        }


class ShelterModel(Base):
    __tablename__ = "shelters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    district = Column(String, index=True)
    capacity = Column(Integer, default=500)
    occupancy = Column(Integer, default=0)
    lat = Column(Float)
    lng = Column(Float)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "district": self.district,
            "capacity": self.capacity,
            "occupancy": self.occupancy,
            "coordinates": {"lat": self.lat, "lng": self.lng} if self.lat and self.lng else None
        }


class RescueTeamModel(Base):
    __tablename__ = "rescue_teams"

    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    type = Column(String)  # NDRF, SDRF, Army Column, Quick Response, Boat Unit
    district = Column(String, index=True)
    personnel_count = Column(Integer, default=10)
    status = Column(String, default="Standby")  # Deployed, Standby, En Route
    lat = Column(Float, nullable=True)
    lng = Column(Float, nullable=True)

    def to_dict(self):
        return {
            "id": self.team_id or str(self.id),
            "name": self.name,
            "type": self.type,
            "district": self.district,
            "personnel_count": self.personnel_count,
            "status": self.status,
            "coordinates": {"lat": self.lat, "lng": self.lng} if self.lat and self.lng else None
        }


class EmergencyAlertModel(Base):
    __tablename__ = "emergency_alerts"

    id = Column(Integer, primary_key=True, index=True)
    alert_id = Column(String, unique=True, index=True)
    type = Column(String)  # Flash Flood Advisory, High Water Warning, Heavy Rain Watch, etc.
    severity = Column(String)  # Critical, Severe, Moderate, Low
    district = Column(String, index=True)
    river = Column(String, nullable=True)
    message = Column(Text)
    issued_by = Column(String, default="Assam State Disaster Management Authority")
    issued_at = Column(DateTime, default=datetime.utcnow)
    valid_until = Column(DateTime)
    status = Column(String, default="Active")

    def to_dict(self):
        return {
            "alert_id": self.alert_id or f"ALT-{self.id}",
            "type": self.type,
            "severity": self.severity,
            "district": self.district,
            "river": self.river,
            "message": self.message,
            "issued_by": self.issued_by,
            "issued_at": self.issued_at.isoformat() if self.issued_at else None,
            "valid_until": self.valid_until.isoformat() if self.valid_until else None,
            "status": self.status
        }


class CitizenReportModel(Base):
    __tablename__ = "citizen_reports"

    id = Column(Integer, primary_key=True, index=True)
    report_id = Column(String, unique=True, index=True)
    reporter_name = Column(String)
    type = Column(String)  # Flooding, Bridge Damage, Trapped People, Shelter Full, Road Blocked
    location = Column(String)
    district = Column(String, index=True)
    description = Column(Text, nullable=True)
    status = Column(String, default="Pending Review")  # Verified, Pending Review, Dispatched
    media_attached = Column(Boolean, default=False)
    submitted_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "report_id": self.report_id or f"REP-{self.id}",
            "reporter_name": self.reporter_name,
            "type": self.type,
            "location": self.location,
            "district": self.district,
            "description": self.description or "",
            "status": self.status,
            "media_attached": self.media_attached,
            "submitted_at": self.submitted_at.isoformat() if self.submitted_at else None
        }


class ResourceItemModel(Base):
    __tablename__ = "resource_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    icon = Column(String, default="ti-package")
    have = Column(Integer, default=0)
    total = Column(Integer, default=100)
    color = Column(String, default="var(--safe)")

    def to_dict(self):
        return {
            "name": self.name,
            "icon": self.icon,
            "have": self.have,
            "total": self.total,
            "color": self.color
        }
