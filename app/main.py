from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.config.database import database, engine, Base, create_tables

@asynccontextmanager
async def lifespan(application: FastAPI):
    await database.connect()
    await create_tables()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

