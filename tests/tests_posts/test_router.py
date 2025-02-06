import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.mark.anyio
async def test_create_post():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000/api"
    ) as ac:
        response = await ac.post(
            url="/posts/create",
            json={
                "image_url": "string_1",
                "image_url_type": "absolute",
                "caption": "string",
                "user_id": 1,
            },
        )
    assert response.status_code == 201
