import motor.motor_asyncio
from core.config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URL)

database = client.career_students