import os

from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN") or ""

DEFAULT_BOT_PROPERTIES = DefaultBotProperties(parse_mode="html")

DEBUG = os.getenv("DEBUG") in ["true", "yes", "True"]

DATABASE_URL = "sqlite://db.sqlite3" if DEBUG else os.getenv("DATABASE_PUBLIC_URL")

WEB_SERVER_HOST = "0.0.0.0"
WEB_SERVER_PORT = 8080
WEBHOOK_SECRET = os.getenv("BOT_WEBHOOK_SECRET") or ""
WEBHOOK_BASE_URL = os.getenv("BOT_WEBHOOK_BASE_URL") or ""
