from sqlalchemy.exc import ProgrammingError
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

from app.config.config import config
from app.config.database import database, setup_db
import pytest
from httpx import AsyncClient, ASGITransport
import anyio

# TEST_DATABASE_URL = f"postgresql+asyncpg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_SERVER}:{config.POSTGRES_PORT}/test_web_app"
# engine = create_async_engine(TEST_DATABASE_URL, echo=True)
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# def create_test_database():
#     async with engine.connect() as conn:
#         try:
#             conn.execute(text("CREATE DATABASE 'test_web_app'"))
#         except ProgrammingError as e:
#             print("Test database already exists")
#
# @pytest.fixture(scope="session", autouse=True)
# def

@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

@pytest.fixture(autouse=True)
async def db():
    await setup_db()
    yield
    await database.close_db()

