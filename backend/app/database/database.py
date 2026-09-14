"""
Varuna AI — Database Connection
SQLAlchemy engine, session, and base model configuration.
"""

import os
import tempfile
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import get_settings

config = get_settings()

BASE_DIR = Path(__file__).resolve().parent

# On Vercel / serverless environments, write SQLite database to /tmp
if (
    os.getenv("VERCEL")
    or os.getenv("AWS_EXECUTION_ENV")
    or not os.access(BASE_DIR, os.W_OK)
):
    DB_PATH = Path(tempfile.gettempdir()) / "varuna.db"
else:
    DB_PATH = BASE_DIR / "varuna.db"

# Use DATABASE_URL from config, fall back to SQLite
SQLALCHEMY_DATABASE_URL = config.DATABASE_URL
if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

# SQLite connection args
connect_args = (
    {"check_same_thread": False} if SQLALCHEMY_DATABASE_URL.startswith("sqlite") else {}
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """FastAPI dependency for database sessions."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
