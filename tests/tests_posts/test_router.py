import pytest


@pytest.mark.anyio
async def test_create_post(get_client, create_user):
    response = await get_client.post(
        url="/posts/create",
        json={
            "image_url": "string_1",
            "image_url_type": "absolute",
            "caption": "string",
            "user_id": 1,
        },
    )
    assert response.status_code == 201
    assert response.json() ==
