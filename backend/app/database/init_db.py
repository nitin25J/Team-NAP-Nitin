from datetime import datetime, timedelta
from app.database.database import engine, Base, SessionLocal
from app.database.db_models import (
    HospitalModel,
    ShelterModel,
    RescueTeamModel,
    EmergencyAlertModel,
    CitizenReportModel,
    ResourceItemModel,
)

def init_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        # Seed Hospitals if empty
        if db.query(HospitalModel).count() == 0:
            hospitals = [
                HospitalModel(name="Guwahati Medical College & Hospital", district="Kamrup Metropolitan", beds_available=45, beds_total=300, icu_available=6, icu_total=40, lat=26.1558, lng=91.7686),
                HospitalModel(name="Sivasagar Civil Hospital", district="Sivasagar", beds_available=12, beds_total=120, icu_available=2, icu_total=15, lat=26.9826, lng=94.6425),
                HospitalModel(name="Silchar Medical College & Hospital", district="Cachar", beds_available=8, beds_total=250, icu_available=1, icu_total=30, lat=24.8333, lng=92.7667),
                HospitalModel(name="Jorhat Medical College & Hospital", district="Jorhat", beds_available=28, beds_total=200, icu_available=5, icu_total=25, lat=26.7509, lng=94.2037),
                HospitalModel(name="Golaghat Civil Hospital", district="Golaghat", beds_available=18, beds_total=100, icu_available=3, icu_total=10, lat=26.5167, lng=93.9667),
                HospitalModel(name="Sonari Civil Hospital", district="Charaideo", beds_available=15, beds_total=80, icu_available=2, icu_total=8, lat=26.9000, lng=94.8800),
            ]
            db.add_all(hospitals)

        # Seed Shelters if empty
        if db.query(ShelterModel).count() == 0:
            shelters = [
                ShelterModel(name="Govt Higher Secondary School Shelter", district="Sivasagar", capacity=400, occupancy=284, lat=26.9850, lng=94.6390),
                ShelterModel(name="Jorhat Indoor Stadium Relief Camp", district="Jorhat", capacity=600, occupancy=320, lat=26.7520, lng=94.2050),
                ShelterModel(name="Golaghat Town Hall Shelter", district="Golaghat", capacity=350, occupancy=190, lat=26.5180, lng=93.9690),
                ShelterModel(name="Silchar District Relief Shelter", district="Cachar", capacity=800, occupancy=650, lat=24.8350, lng=92.7700),
                ShelterModel(name="Guwahati Sector 3 Relief Center", district="Kamrup Metropolitan", capacity=500, occupancy=185, lat=26.1480, lng=91.7400),
            ]
            db.add_all(shelters)

        # Seed Rescue Teams if empty
        if db.query(RescueTeamModel).count() == 0:
            teams = [
                RescueTeamModel(team_id="NDRF-ALPHA", name="NDRF Team Alpha", type="NDRF Battalion 12", district="Sivasagar", personnel_count=45, status="Deployed", lat=26.9830, lng=94.6400),
                RescueTeamModel(team_id="SDRF-BRAVO", name="SDRF Unit Bravo", type="SDRF State Force", district="Golaghat", personnel_count=30, status="Deployed", lat=26.5170, lng=93.9680),
                RescueTeamModel(team_id="ARMY-CHARLIE", name="Indian Army Column 4", type="Military Relief", district="Cachar", personnel_count=60, status="Deployed", lat=24.8340, lng=92.7680),
                RescueTeamModel(team_id="BOAT-UNIT-01", name="Sivasagar Motorboat Unit", type="Inflatable Boat Fleet", district="Sivasagar", personnel_count=12, status="Deployed", lat=26.9810, lng=94.6450),
                RescueTeamModel(team_id="QRT-DELTA", name="Guwahati Quick Response", type="Medical Evac QRT", district="Kamrup Metropolitan", personnel_count=20, status="Standby", lat=26.1450, lng=91.7370),
            ]
            db.add_all(teams)

        # Seed Emergency Alerts if empty
        if db.query(EmergencyAlertModel).count() == 0:
            now = datetime.utcnow()
            alerts = [
                EmergencyAlertModel(
                    alert_id="ALT-101",
                    type="Flash Flood & River Breach Warning",
                    severity="Critical",
                    district="Sivasagar",
                    river="Brahmaputra & Dikhow",
                    message="Water levels rising past danger mark by 1.8m. Low-lying wards 4-7 instructed to evacuate immediately to designated relief shelters.",
                    issued_by="Assam State Disaster Management Authority",
                    issued_at=now - timedelta(hours=2),
                    valid_until=now + timedelta(hours=14),
                    status="Active"
                ),
                EmergencyAlertModel(
                    alert_id="ALT-102",
                    type="Heavy Rainfall & Landslide Watch",
                    severity="Severe",
                    district="Charaideo",
                    river="Disang",
                    message="Continuous heavy precipitation expected for next 24 hours. High vulnerability of hill slopes to saturation and landslides.",
                    issued_by="India Meteorological Department (IMD)",
                    issued_at=now - timedelta(hours=1),
                    valid_until=now + timedelta(hours=18),
                    status="Active"
                ),
                EmergencyAlertModel(
                    alert_id="ALT-103",
                    type="Urban Waterlogging Advisory",
                    severity="Moderate",
                    district="Kamrup Metropolitan",
                    river="Bharalu",
                    message="Waterlogging reported across primary arterial roads. Citizens advised to avoid underpasses and riverfront zones.",
                    issued_by="Guwahati Municipal Corporation",
                    issued_at=now - timedelta(minutes=45),
                    valid_until=now + timedelta(hours=8),
                    status="Active"
                ),
            ]
            db.add_all(alerts)

        # Seed Citizen Reports if empty
        if db.query(CitizenReportModel).count() == 0:
            now = datetime.utcnow()
            reports = [
                CitizenReportModel(
                    report_id="REP-901",
                    reporter_name="Bhaben Kalita",
                    type="Flooding",
                    location="Riverside colony, Ward 4",
                    district="Sivasagar",
                    description="Flood water entered houses up to waist height. 15 families stranded on rooftops requiring boat rescue.",
                    status="Verified",
                    media_attached=True,
                    submitted_at=now - timedelta(minutes=25)
                ),
                CitizenReportModel(
                    report_id="REP-902",
                    reporter_name="Priyanka Gogoi",
                    type="Bridge Damage",
                    location="Sector 12 approach bridge",
                    district="Golaghat",
                    description="Approach embankment eroded by fast current. Light vehicles stranded on both sides.",
                    status="Verified",
                    media_attached=True,
                    submitted_at=now - timedelta(minutes=50)
                ),
                CitizenReportModel(
                    report_id="REP-903",
                    reporter_name="Anil Saikia",
                    type="Road Blocked",
                    location="Market road junction",
                    district="Charaideo",
                    description="Fallen trees and water accumulation blocking emergency vehicles.",
                    status="Pending Review",
                    media_attached=False,
                    submitted_at=now - timedelta(hours=1, minutes=10)
                ),
            ]
            db.add_all(reports)

        # Seed Resource Items if empty
        if db.query(ResourceItemModel).count() == 0:
            resources = [
                ResourceItemModel(name="Ambulances", icon="ti-ambulance", have=34, total=48, color="var(--alert)"),
                ResourceItemModel(name="Fire trucks", icon="ti-flame", have=11, total=16, color="var(--warn)"),
                ResourceItemModel(name="Boats", icon="ti-anchor", have=22, total=30, color="var(--hydro)"),
                ResourceItemModel(name="Rescue helicopters", icon="ti-helicopter", have=4, total=6, color="var(--violet)"),
                ResourceItemModel(name="Medical kits", icon="ti-first-aid-kit", have=860, total=1200, color="var(--safe)"),
                ResourceItemModel(name="Food supplies", icon="ti-bread", have=640, total=1000, color="var(--warn)"),
                ResourceItemModel(name="Water supplies", icon="ti-droplet", have=410, total=900, color="var(--blue)"),
                ResourceItemModel(name="Volunteers", icon="ti-users", have=312, total=400, color="var(--safe)"),
            ]
            db.add_all(resources)

        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized and seeded successfully.")
