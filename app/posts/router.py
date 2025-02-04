from fastapi import APIRouter, status

from app.config.dependencies import SessionDep
from app.posts.schemas import Post, PostIn
from app.posts.services import create_post

posts_router = APIRouter()


@posts_router.post(
    path="/create", status_code=status.HTTP_201_CREATED, response_model=Post
)
async def post_create(session: SessionDep, request: PostIn):
    return await create_post(session, request)
