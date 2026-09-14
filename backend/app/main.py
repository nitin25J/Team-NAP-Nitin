"""
Varuna AI — Application Entry Point
FastAPI application with clean router registration and lifecycle management.
"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings

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

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifecycle — startup and shutdown."""
    # Startup
    logger.info("Varuna AI starting up...")
    
    try:
        from app.database.database import engine
        from app.database.models import Base
        logger.info("Ensuring database tables exist...")
        Base.metadata.create_all(bind=engine)
        
        # We need to import init_db to seed. Since init_db is in backend root:
        import sys
        from pathlib import Path
        root_dir = Path(__file__).resolve().parent.parent.parent
        if str(root_dir) not in sys.path:
            sys.path.insert(0, str(root_dir))
            
        import init_db
        init_db.seed_db()
    except Exception as e:
        logger.error(f"Error initializing/seeding database: {e}")

    yield
    # Shutdown
    logger.info("Varuna AI shutting down.")


config = get_settings()

app = FastAPI(
    title="Varuna AI API",
    description="AI-Powered Disaster Intelligence Platform — Predict. Prepare. Protect.",
    version=config.APP_VERSION,
    lifespan=lifespan,
)

# ------------------------
# CORS Configuration
# ------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.cors_origins_list,
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
        "message": "Welcome to Varuna AI API",
        "version": config.APP_VERSION,
        "status": "running",
    }


@app.get("/health", tags=["Health"])
def health_check_root():
    return {
        "status": "healthy",
        "service": "Varuna AI Backend",
        "version": config.APP_VERSION,
    }


# ------------------------
# Register Routers under /api prefix only (single registration)
# ------------------------
api_router = APIRouter(prefix="/api")

@api_router.get("/health", tags=["Health"])
def api_health_check():
    return {
        "status": "healthy",
        "service": "Varuna AI Backend",
        "version": config.APP_VERSION,
    }

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

app.include_router(api_router)
