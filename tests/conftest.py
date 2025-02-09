import pytest
from httpx import ASGITransport, AsyncClient

from app.config.database import database, setup_db
from app.main import app
from tests.tests_users.services import create_post_for_test, create_user_for_tests


@pytest.fixture()
async def get_client():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000/api"
    ) as client:
        yield client


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(autouse=True)
async def db():
    await database.clear_tables()
    await setup_db()
    yield
    await database.close_db()


@pytest.fixture()
async def create_user(get_client):
    user = {
        "email": "test_2@gmail.com",
        "username": "test user",
        "password": "qwerasdf123",
    }
    return await create_user_for_tests(user, get_client)


@pytest.fixture()
async def create_post(get_client):
    post = {
        "image_url": "string",
        "image_url_type": "absolute",
        "caption": "string",
        "user_id": 1,
    }
    return await create_post_for_test(post, get_client)
