import os
import logging
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from app.database.init_db import init_db

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

logger = logging.getLogger(__name__)

# Initialize SQLite database and seed baseline data
try:
    init_db()
except Exception as e:
    logger.warning("Database init on startup note: %s", e)

app = FastAPI(
    title="Varuna AI API",
    description="AI-Powered Flood Prediction and Disaster Management System",
    version="1.0.0",
)

# ------------------------
# CORS Configuration
# ------------------------
cors_origins_env = os.getenv("CORS_ORIGINS", "*")
origins = (
    [o.strip() for o in cors_origins_env.split(",")]
    if cors_origins_env != "*"
    else ["*"]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins if origins else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ------------------------
# Root & Health Check
# ------------------------
@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to Varuna AI API 🚀",
        "version": "1.0.0",
        "status": "running",
    }


@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "service": "Varuna AI Backend",
    }


# ------------------------
# Register Routers (Both /api prefix and root for full compatibility)
# ------------------------
api_router = APIRouter(prefix="/api")
all_routers = [
    alerts.router,
    analytics.router,
    chatbot.router,
    dashboard.router,
    disaster_map.router,
    hospitals.router,
    prediction.router,
    reports.router,
    rescue.router,
    resources.router,
    satellite.router,
    settings.router,
    weather.router,
]

for r in all_routers:
    api_router.include_router(r)
    app.include_router(r)

app.include_router(api_router)
