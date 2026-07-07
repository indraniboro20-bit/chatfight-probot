import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# MongoDB
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME", "ChatFight")

# Owner
OWNER_ID = int(os.getenv("OWNER_ID"))

# Bot
BOT_NAME = "ChatFight"
BOT_USERNAME = "YourBotUsername"

# Start Image URL
START_IMAGE = "https://graph.org/file/YOUR_START_IMAGE.jpg"

# Buttons
UPDATES_CHANNEL = "https://t.me/YourUpdatesChannel"
SUPPORT_GROUP = "https://t.me/YourSupportGroup"

# Ranking
TIMEZONE = "Asia/Kolkata"
TOP_LIMIT = 20
