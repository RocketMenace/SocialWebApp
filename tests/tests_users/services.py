from typing import Any

from httpx import AsyncClient


async def create_user_for_tests(body: dict[str, Any], async_client: AsyncClient):
    response = await async_client.post("/users/register", json=body)
    return response.json()


async def create_post_for_test(body: dict[str, Any], async_client: AsyncClient):
    response = await async_client.post("/posts/create", json=body)
    return response.json()
