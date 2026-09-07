import os
import tempfile
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

BASE_DIR = Path(__file__).resolve().parent

# On Vercel / serverless environments, write SQLite database to /tmp to avoid Read-Only filesystem errors
if (
    os.getenv("VERCEL")
    or os.getenv("AWS_EXECUTION_ENV")
    or not os.access(BASE_DIR, os.W_OK)
):
    DB_PATH = Path(tempfile.gettempdir()) / "varuna.db"
else:
    DB_PATH = BASE_DIR / "varuna.db"

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DB_PATH}")

# SQLite connection args
connect_args = (
    {"check_same_thread": False} if SQLALCHEMY_DATABASE_URL.startswith("sqlite") else {}
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
