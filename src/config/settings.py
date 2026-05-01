import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")  # ← removed "config" from the path

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")

FIGHTERS = [
    "conor-mcgregor",
    "khabib-nurmagomedov",
    "jon-jones",
    "israel-adesanya",
    "kamaru-usman",
    "georges-st-pierre",
    "max-holloway",
    "jose-aldo",
    "demetrious-johnson",
    "bj-penn",
    "daniel-cormier"
]