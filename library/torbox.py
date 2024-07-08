import os
from dotenv import load_dotenv
load_dotenv()

TORBOX_API_KEY = os.getenv("TORBOX_API_KEY")
TORBOX_API_URL = "https://api.torbox.app/v1/api"