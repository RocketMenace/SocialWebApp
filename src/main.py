from typing import AsyncGenerator
from src.database import Base, engine
from src.users.router import users_router

from fastapi import FastAPI
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(_application: FastAPI) -> AsyncGenerator:
    Base.metadata.create_all(engine)
    yield


app = FastAPI(root_path="/api", lifespan=lifespan)

app.include_router(users_router, prefix="/users", tags=["users"])
