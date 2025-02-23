from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.auth.jwt import check_user_jwt
from app.auth.schemas import JWTData
from app.config.dependencies import SessionDep
from app.posts.schemas import Post, PostIn
from app.posts.services import create_post, delete_post, get_posts

posts_router = APIRouter()


@posts_router.post(
    path="/create", status_code=status.HTTP_201_CREATED, response_model=Post
)
async def post_create(session: SessionDep, request: PostIn, token: Annotated[JWTData | None, Depends(check_user_jwt)]):
    return await create_post(session, request, token)


@posts_router.get(path="", status_code=status.HTTP_200_OK, response_model=list[Post])
async def post_list(session: SessionDep):
    return await get_posts(session)


@posts_router.delete(path="/delete/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def post_delete(
    post_id: int,
    session: SessionDep,
    token: Annotated[JWTData | None, Depends(check_user_jwt)],
):
    await delete_post(session, post_id, token)
