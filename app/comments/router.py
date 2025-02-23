from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.auth.jwt import check_user_jwt
from app.auth.schemas import JWTData
from app.comments.schemas import Comment, CommentIn
from app.comments.services import create_comment, get_all_comments
from app.config.dependencies import SessionDep
from app.posts.schemas import Post

comments_router = APIRouter()


@comments_router.get(
    path="/{post_id}", status_code=status.HTTP_200_OK, response_model=list[Comment]
)
async def comments(session: SessionDep, post_id: int):
    return await get_all_comments(session, post_id)


@comments_router.post(
    path="/create", status_code=status.HTTP_201_CREATED, response_model=Comment
)
async def comment_create(
    session: SessionDep,
    request: CommentIn,
    token: Annotated[JWTData | None, Depends(check_user_jwt)],
):
    return await create_comment(session, request, token)
