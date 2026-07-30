from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import all routers
from app.api import (
    alerts,
    analytics,
    chatbot,
    dashboard,
    disaster_map,
    hospitals,
    prediction,
    reports,
    rescue,
    resources,
    satellite,
    settings,
    weather,
)

app = FastAPI(
    title="Varuna AI API",
    description="AI-Powered Flood Prediction and Disaster Management System",
    version="1.0.0",
)

# ------------------------
# CORS Configuration
# ------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Change this later in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------
# Root Endpoint
# ------------------------
@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to Varuna AI API 🚀",
        "version": "1.0.0",
        "status": "running",
    }


# ------------------------
# Health Check
# ------------------------
@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "service": "Varuna AI Backend",
    }


# ------------------------
# Register Routers
# ------------------------

app.include_router(alerts.router)
app.include_router(analytics.router)
app.include_router(chatbot.router)
app.include_router(dashboard.router)
app.include_router(disaster_map.router)
app.include_router(hospitals.router)
app.include_router(prediction.router)
app.include_router(reports.router)
app.include_router(rescue.router)
app.include_router(resources.router)
app.include_router(satellite.router)
app.include_router(settings.router)
app.include_router(weather.router)