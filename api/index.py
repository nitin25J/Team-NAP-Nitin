import sys
import os
from pathlib import Path

# Add backend directory to Python sys.path
BASE_DIR = Path(__file__).resolve().parent.parent / "backend"
sys.path.insert(0, str(BASE_DIR))

from app.main import app

# Export app for Vercel Serverless
__all__ = ["app"]
