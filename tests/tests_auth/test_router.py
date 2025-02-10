import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_user_login_invalid_credentials(get_client: AsyncClient):
    response = await get_client.post(
        url="/auth/login", json={"email": "bob@gmail.com", "password": "qwerasdf"}
    )
    assert response.status_code == 400


@pytest.mark.anyio
async def test_user_login(get_client: AsyncClient, create_user):
    response = await get_client.post(
        "/auth/login",
        json={"email": create_user["email"], "password": "qwerasdf123"},
    )
    assert response.status_code == 200
