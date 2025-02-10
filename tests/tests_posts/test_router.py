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
    assert (
        response.json().items()
        >= {
            "image_url": "string_1",
            "image_url_type": "absolute",
            "caption": "string",
            "user_id": 1,
        }.items()
    )


@pytest.mark.anyio
async def test_create_post_missing_data(get_client):
    response = await get_client.post("/posts/create", json={})
    assert response.status_code == 422


@pytest.mark.anyio
async def test_get_all_posts(get_client, create_user, create_post):
    response = await get_client.get("/posts")
    assert response.status_code == 200
    assert response.json() == [create_post]


@pytest.mark.anyio
async def test_delete_post(get_client, create_user, create_post):
    response = await get_client.delete(f"/posts/delete/{create_post['id']}")
    assert response.status_code == 204
