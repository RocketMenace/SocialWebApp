from typing import AsyncGenerator
from database import Base, engine

from fastapi import FastAPI
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(_application: FastAPI) -> AsyncGenerator:
    Base.metadata.create_all(engine)
    yield


app = FastAPI()
