import motor.motor_asyncio
from dotenv import load_dotenv
import os

load_dotenv()

DB_SERVER = os.getenv("DB_SERVER")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_URL = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}"

client = motor.motor_asyncio.AsyncIOMotorClient(DB_URL)
database = client.readmewriter