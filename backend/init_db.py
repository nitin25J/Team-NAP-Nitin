import os
from datetime import datetime, timedelta
from app.database.database import SessionLocal, engine, Base
from app.database.models import Hospital, RescueTeam, Incident, Resource, Prediction, WeatherForecast

def init_db():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)

def seed_db():
    db = SessionLocal()
    
    # Check if we already have data
    if db.query(Hospital).first():
        print("Database already seeded.")
        db.close()
        return

    print("Seeding database with realistic Assam disaster data...")

    # 1. Seed Hospitals
    hospitals = [
        Hospital(name="Guwahati Medical College (GMCH)", district="Kamrup Metropolitan", beds_total=1200, beds_available=145, icu_total=150, icu_available=12, oxygen_available=True, status="Critical Load"),
        Hospital(name="Jorhat Medical College", district="Jorhat", beds_total=850, beds_available=210, icu_total=80, icu_available=18, oxygen_available=True, status="High Load"),
        Hospital(name="Silchar Medical College", district="Cachar", beds_total=900, beds_available=85, icu_total=100, icu_available=4, oxygen_available=False, status="Critical - No O2"),
        Hospital(name="Sivasagar Civil Hospital", district="Sivasagar", beds_total=400, beds_available=120, icu_total=30, icu_available=15, oxygen_available=True, status="Operational"),
        Hospital(name="Majuli District Hospital", district="Majuli", beds_total=150, beds_available=10, icu_total=10, icu_available=0, oxygen_available=True, status="Extreme Load"),
    ]
    db.add_all(hospitals)

    # 2. Seed Rescue Teams
    teams = [
        RescueTeam(name="NDRF 1st Battalion Alpha", type="NDRF", location="Guwahati Base", personnel_count=45, status="Standby"),
        RescueTeam(name="NDRF 1st Battalion Bravo", type="NDRF", location="Majuli", personnel_count=45, status="Deployed"),
        RescueTeam(name="SDRF Riverine Unit 1", type="SDRF", location="Silchar", personnel_count=20, status="Deployed"),
        RescueTeam(name="Indian Army Column 4", type="Military", location="Jorhat", personnel_count=120, status="Deployed"),
        RescueTeam(name="SDRF Quick Response", type="SDRF", location="Kaziranga", personnel_count=15, status="En-route"),
    ]
    db.add_all(teams)

    # 3. Seed Incidents
    incidents = [
        Incident(reporter_name="B. Phukan", location="Majuli South Bank", description="Embankment breached, severe flooding entering villages.", severity="Critical", verified=True, status="Dispatched"),
        Incident(reporter_name="Anonymous", location="Kaziranga NH37", description="Highway submerged, animals stranded.", severity="High", verified=True, status="Pending"),
        Incident(reporter_name="P. Das", location="Silchar Town", description="Water level rising rapidly, ground floors flooded.", severity="High", verified=False, status="Pending"),
        Incident(reporter_name="R. Gogoi", location="Sivasagar", description="Power outage and minor flooding in low lying areas.", severity="Moderate", verified=True, status="Pending"),
    ]
    db.add_all(incidents)

    # 4. Seed Resources (Inventory & Shelters - mapped slightly differently, but we store inventory here)
    resources = [
        Resource(name="Inflatable Boats", type="Equipment", total_quantity=150, available_quantity=45, district="Kamrup"),
        Resource(name="Life Jackets", type="Equipment", total_quantity=2000, available_quantity=850, district="Kamrup"),
        Resource(name="Food Packets (MREs)", type="Relief", total_quantity=50000, available_quantity=12000, district="Jorhat"),
        Resource(name="Portable Generators", type="Equipment", total_quantity=100, available_quantity=12, district="Cachar"),
        Resource(name="Medical Kits", type="Medical", total_quantity=5000, available_quantity=800, district="Kamrup"),
    ]
    db.add_all(resources)

    # 5. Seed Predictions
    predictions = [
        Prediction(
            district="Majuli",
            risk_level="Extreme Risk",
            severity_score=92.5,
            water_level_m=87.2,
            danger_mark_m=85.5,
            rainfall_mm_24h=145.0,
            confidence=0.94,
            recommendations=["Immediate evacuation of lower river banks", "Deploy SDRF Riverine Unit", "Prepare relief camps at higher elevation"]
        ),
        Prediction(
            district="Cachar",
            risk_level="High Risk",
            severity_score=84.0,
            water_level_m=20.5,
            danger_mark_m=19.8,
            rainfall_mm_24h=95.0,
            confidence=0.88,
            recommendations=["Monitor Barak river embankment", "Pre-position medical supplies"]
        ),
        Prediction(
            district="Kamrup Metropolitan",
            risk_level="Moderate Risk",
            severity_score=65.0,
            water_level_m=49.1,
            danger_mark_m=49.6,
            rainfall_mm_24h=45.0,
            confidence=0.91,
            recommendations=["Clear urban drainage systems", "Issue heavy rain advisory to public"]
        )
    ]
    db.add_all(predictions)

    db.commit()
    db.close()
    print("Database seeding complete!")

if __name__ == "__main__":
    init_db()
    seed_db()
