from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.schemas import JWTData
from app.comments.models import Comment
from app.comments.schemas import CommentIn
from app.posts.models import Post


async def create_comment(session: AsyncSession, request: CommentIn, token: JWTData):
    new_comment = Comment(
        text=request.text,
        username=request.username,
        post_id=request.post_id,
        user_id=token.user_id,
    )
    session.add(new_comment)
    await session.commit()
    await session.refresh(new_comment)
    return new_comment


async def get_all_comments(session: AsyncSession, post_id: int):
    return await session.scalars(select(Comment).where(Comment.post_id == post_id))
