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
    contact = Column(String, default="+91 361 2529457")
    status = Column(String, default="Operational")

    def to_dict(self):
        avail = self.beds_available or 0
        total = self.beds_total or 100
        is_low = avail < 15
        calc_status = self.status or ("High Load" if is_low else "Operational")
        return {
            "id": self.id,
            "name": self.name,
            "district": self.district,
            "beds_available": avail,
            "beds_total": total,
            "icu_available": self.icu_available or 0,
            "icu_total": self.icu_total or 20,
            "icu_beds": self.icu_available or 0,
            "oxygen_available": True,
            "status": calc_status,
            "contact": self.contact or "+91 361 2529457",
            "lat": self.lat,
            "lng": self.lng,
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
            "capacity": self.capacity or 500,
            "occupancy": self.occupancy or 0,
            "lat": self.lat,
            "lng": self.lng,
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
            "team_id": self.team_id or str(self.id),
            "name": self.name,
            "type": self.type,
            "district": self.district,
            "location": self.district,
            "members": self.personnel_count or 10,
            "personnel_count": self.personnel_count or 10,
            "status": (self.status or "Standby").lower(),
            "lat": self.lat,
            "lng": self.lng,
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
        sev = (self.severity or "Severe").lower()
        is_crit = sev == "critical"
        return {
            "id": self.id,
            "alert_id": self.alert_id or f"ALT-{self.id}",
            "type": self.type,
            "title": f"{self.type} — {self.district}",
            "severity": self.severity or "Severe",
            "level": "critical" if is_crit else "warning",
            "district": self.district,
            "districts": self.district,
            "river": self.river,
            "message": self.message,
            "population": "1.2 L",
            "confidence": 91,
            "endsIn": 10800,
            "issued_by": self.issued_by,
            "issued_at": self.issued_at.isoformat() if self.issued_at else None,
            "valid_until": self.valid_until.isoformat() if self.valid_until else None,
            "status": self.status or "Active"
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
            "id": self.id,
            "report_id": self.report_id or f"REP-{self.id}",
            "reporter_name": self.reporter_name or "Anonymous citizen",
            "user": self.reporter_name or "Anonymous citizen",
            "type": self.type,
            "location": f"{self.location}, {self.district}" if self.location and self.district and self.district not in self.location else (self.location or self.district),
            "district": self.district,
            "description": self.description or "",
            "severity": "critical" if "critical" in (self.description or "").lower() or "flood" in (self.type or "").lower() else "moderate",
            "status": self.status or "Verified",
            "verified": self.media_attached or (self.status or "").lower() in ["verified", "dispatched", "en route"],
            "media_attached": self.media_attached,
            "time": "Just now" if not self.submitted_at else "Recently",
            "submitted_at": self.submitted_at.isoformat() if self.submitted_at else None,
            "image": "https://images.unsplash.com/photo-1657069343871-fd1476990d04?auto=format&fit=crop&w=1200&q=80"
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
            "id": self.id,
            "name": self.name,
            "icon": self.icon or "ti-package",
            "have": self.have or 0,
            "total": self.total or 100,
            "color": self.color or "var(--safe)"
        }
