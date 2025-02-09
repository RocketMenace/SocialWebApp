import pytest


@pytest.mark.anyio
async def test_user_register(get_client):
    response = await get_client.post(
        url="/users/register",
        json={
            "email": "test_2@gmail.com",
            "username": "test user",
            "password": "qwerasdf123",
        },
    )
    assert response.status_code == 201
    assert response.json() == {"username": "test user", "email": "test_2@gmail.com"}


@pytest.mark.anyio
async def test_user_register_invalid_data(get_client, create_user):
    response = await get_client.post(
        "/users/register",
        json={
            "email": "test_2@gmail.com",
            "username": "test user",
            "password": "qwerasdf123",
        },
    )
    assert response.status_code == 400
