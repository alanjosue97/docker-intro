from motor.motor_asyncio import AsyncIOMotorClient

async def get_db():
    client = AsyncIOMotorClient("mongodb+srv://academia:academia@cluster0.mtpqpfb.mongodb.net/?retryWrites=true&w=majority")
    return client.academia