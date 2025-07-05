import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN not found in .env file")
if not CHAT_ID:
    raise ValueError("❌ CHAT_ID not found in .env file")

CHAT_ID = int(CHAT_ID)
