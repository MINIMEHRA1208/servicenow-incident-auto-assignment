import os
from dotenv import load_dotenv

load_dotenv()

SNOW_INSTANCE = os.getenv("SNOW_INSTANCE")
SNOW_USERNAME = os.getenv("SNOW_USERNAME")
SNOW_PASSWORD = os.getenv("SNOW_PASSWORD")

DEFAULT_ASSIGNMENT_GROUP = "Service Desk"
