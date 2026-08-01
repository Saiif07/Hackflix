"""
Config loader for Hackflix
"""
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    ADMIN_IDS: list = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip()]
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///hackflix.db")

settings = Settings()
