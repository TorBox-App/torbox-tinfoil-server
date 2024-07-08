import os
from dotenv import load_dotenv
load_dotenv()

AUTH_USERNAME = os.getenv("AUTH_USERNAME")
AUTH_PASSWORD = os.getenv("AUTH_PASSWORD")
PORT = os.getenv("PORT")
