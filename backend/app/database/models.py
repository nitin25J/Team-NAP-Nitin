from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Text, JSON, func
from .database import Base

class Hospital(Base):
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    district = Column(String, index=True)
    beds_total = Column(Integer, default=0)
    beds_available = Column(Integer, default=0)
    icu_total = Column(Integer, default=0)
    icu_available = Column(Integer, default=0)
    oxygen_available = Column(Boolean, default=True)
    status = Column(String, default="Operational")
    last_updated = Column(DateTime(timezone=True), onupdate=func.now())

class RescueTeam(Base):
    __tablename__ = "rescue_teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)  # NDRF, SDRF, Military, etc.
    location = Column(String, index=True)
    personnel_count = Column(Integer, default=0)
    status = Column(String, default="Standby")  # Deployed, Standby, En-route
    last_updated = Column(DateTime(timezone=True), onupdate=func.now())

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    reporter_name = Column(String)
    location = Column(String, index=True)
    description = Column(Text)
    severity = Column(String)  # Critical, High, Moderate, Low
    image_url = Column(String, nullable=True)
    verified = Column(Boolean, default=False)
    status = Column(String, default="Pending")  # Pending, Dispatched, Resolved
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    total_quantity = Column(Integer, default=0)
    available_quantity = Column(Integer, default=0)
    district = Column(String, index=True)

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    district = Column(String, index=True)
    risk_level = Column(String)
    severity_score = Column(Float)
    water_level_m = Column(Float)
    danger_mark_m = Column(Float)
    rainfall_mm_24h = Column(Float)
    confidence = Column(Float)
    recommendations = Column(JSON)  # List of strings
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

class WeatherForecast(Base):
    __tablename__ = "weather_forecasts"

    id = Column(Integer, primary_key=True, index=True)
    district = Column(String, index=True)
    date = Column(String)
    temperature_max = Column(Float)
    temperature_min = Column(Float)
    rainfall_mm = Column(Float)
    description = Column(String)
