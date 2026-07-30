# Varuna AI

### AI Disaster Intelligence Platform

**Tagline:** *Predict. Prepare. Protect.*

---

## Overview

Varuna AI is an AI-powered Disaster Intelligence Platform designed to improve disaster preparedness and emergency response through centralized monitoring and intelligent decision support.

The platform integrates weather intelligence, disaster mapping, emergency resources, hospitals, rescue operations, and analytics into a unified dashboard for government agencies and disaster management authorities.

The current prototype focuses on flood disaster management in Assam and is designed to scale for multiple disaster types and regions.

---

## Live Demo

**Frontend:** https://varuna-ai.vercel.app/

**Backend API:** https://varuna-ai.onrender.com/

**API Documentation (Swagger):** https://varuna-ai.onrender.com/docs

---

## Vision

Build an intelligent disaster management ecosystem that enables proactive decision-making using Artificial Intelligence.

---

## Key Features

- Real-Time Dashboard
- Weather Intelligence
- Interactive Disaster Map
- Flood Risk Prediction *(Prototype)*
- Emergency Alerts
- Hospital Monitoring
- Rescue Team Management
- Resource Management
- Reports & Analytics
- Responsive Dashboard UI

---

## System Architecture

```text
Weather Data
Satellite Data
GIS Data
Hospital Data
Rescue Data
        │
        ▼
     FastAPI Backend
        │
 ├── Dashboard
 ├── Weather
 ├── Alerts
 ├── Prediction
 ├── Hospitals
 ├── Resources
 ├── Rescue
 ├── Reports
 └── Analytics
        │
        ▼
 JSON Data Layer
(Current Prototype)

Future:
PostgreSQL • PostGIS • Neo4j
```

---

## Frontend Architecture

```text
Browser
    │
    ▼
HTML • CSS • JavaScript
    │
    ▼
Dashboard Components
    │
    ▼
API Layer (config.js)
    │
    ▼
FastAPI Backend
```

---

## Backend Architecture

```text
FastAPI
│
├── API Routes
│
├── /dashboard
├── /alerts
├── /weather
├── /prediction
├── /hospitals
├── /resources
├── /rescue
├── /reports
├── /analytics
├── /settings
└── /disaster-map
│
▼
Service Layer
│
├── dashboard_service.py
├── alert_service.py
├── weather_service.py
├── prediction_service.py
├── hospital_service.py
├── resource_service.py
├── rescue_service.py
├── report_service.py
├── analytics_service.py
└── disaster_map_service.py
│
▼
Database Loader
│
▼
JSON Dataset (Current Prototype)
```

---

## Technology Stack

### Frontend

- HTML5
- CSS3
- JavaScript (ES6)
- Leaflet.js
- Chart.js
- Responsive Design

### Backend

- FastAPI
- Python
- Pydantic
- Uvicorn

### Current Data Layer

- JSON Dataset

### Planned Technologies

- PostgreSQL
- PostGIS
- Neo4j
- LangChain
- OpenAI / Gemini
- TensorFlow
- PyTorch
- OpenCV
- Multi-Agent AI
- Digital Twin

---

## Deployment

| Component | Platform |
|-----------|----------|
| Frontend | Vercel |
| Backend | Render |

---

## Repository Structure

```text
VarunaAI/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── services/
│   │   ├── database/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── core/
│   │   └── utils/
│   │
│   ├── requirements.txt
│   ├── Dockerfile
│   └── main.py
│
├── frontend/
│   ├── css/
│   ├── js/
│   ├── assets/
│   └── index.html
│
├── docs/
├── assets/
├── README.md
├── LICENSE
└── .gitignore
```

---

## Project Status

### Implemented

- Interactive Frontend Dashboard
- FastAPI Backend
- REST API Architecture
- Dashboard Module
- Weather Module
- Disaster Map
- Alerts
- Hospitals
- Rescue Operations
- Resources
- Reports
- Analytics
- JSON-Based Data Layer

### In Progress

- Frontend–Backend Integration
- Live Weather API Integration

### Planned

- AI Prediction Models
- PostgreSQL Migration
- Knowledge Graph
- Digital Twin
- Multi-Agent AI
- IoT Integration
- Citizen Mobile Application

---

## Future Scope

- Real-Time Satellite Data
- IoT Sensor Integration
- Explainable AI
- Digital Twin Simulation
- Intelligent Resource Optimization
- National-Scale Deployment

---

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

## License

This project is licensed under the **MIT License**.

---

## Varuna AI

**Predict. Prepare. Protect.**
