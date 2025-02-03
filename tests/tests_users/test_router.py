import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.anyio
async def test_user_register():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000/api"
    ) as ac:
        response = await ac.post(
            url="/users/register",
            json={
                "email": "test_2@gmail.com",
                "username": "test user",
                "password": "qwerasdf123",
            },
        )
        assert response.status_code == 201
        assert response.json() == {"username": "test user", "email": "test_2@gmail.com"}
