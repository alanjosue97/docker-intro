from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_INITDB_ROOT_USERNAME= os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_INITDB_ROOT_PASSWORD= os.getenv("MONGO_INITDB_ROOT_PASSWORD")


async def get_db():
    client = AsyncIOMotorClient(f"mongodb+srv://{MONGO_INITDB_ROOT_USERNAME}:{MONGO_INITDB_ROOT_PASSWORD}@cluster0.mtpqpfb.mongodb.net/?retryWrites=true&w=majority")
    return client.academia