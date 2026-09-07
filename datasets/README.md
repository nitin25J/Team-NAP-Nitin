# Varuna AI — Assam National Disaster Intelligence Datasets

This directory contains standalone, structured datasets for disaster response management across **10 flood-prone districts of Assam, India**:
* **Kamrup Metropolitan (Guwahati)**
* **Sivasagar**
* **Jorhat**
* **Golaghat**
* **Dibrugarh**
* **Cachar (Silchar)**
* **Charaideo**
* **Lakhimpur**
* **Dhemaji**
* **Nagaon**

---

## 📂 Dataset Files Included

| Dataset File | Format | Description |
| :--- | :--- | :--- |
| `assam_hospitals_dataset.json` / `.csv` | JSON / CSV | 10 major civil & medical college hospitals with bed capacity, ICU availability, oxygen status, and coordinates |
| `assam_shelters_dataset.json` / `.csv` | JSON / CSV | Emergency relief camps & school shelters with total capacity and live occupancy |
| `assam_rescue_units_dataset.json` / `.csv` | JSON / CSV | NDRF, SDRF, Indian Army columns, and motorboat response teams |
| `assam_emergency_alerts_dataset.json` / `.csv` | JSON / CSV | Active flash flood, river level breach, and landslide advisories |
| `assam_citizen_reports_dataset.json` / `.csv` | JSON / CSV | Crowd-sourced distress reports with AI verification status and coordinates |
| `assam_disaster_resources_dataset.json` / `.csv` | JSON / CSV | Inventory logistics (ambulances, motorboats, medical kits, food rations, helicopters) |
| `assam_river_gauge_dataset.json` / `.csv` | JSON / CSV | Hydrological gauge stations for Brahmaputra, Dikhow, Disang, Dhansiri, Subansiri & Barak rivers |

---

## 🛠️ Usage in Varuna AI
These datasets are automatically seeded into the application database (`varuna.db`) on backend startup via `backend/app/database/init_db.py`.
