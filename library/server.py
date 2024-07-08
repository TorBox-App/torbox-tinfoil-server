import os
from dotenv import load_dotenv

load_dotenv()

AUTH_USERNAME = os.getenv("AUTH_USERNAME", "admin")
AUTH_PASSWORD = os.getenv("AUTH_PASSWORD", "adminadmin")
PORT = os.getenv("PORT", 8000)
