from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.schemas import JWTData
from app.posts.exceptions import DeletionRestricted, PostNotFound
from app.posts.models import Post
from app.posts.schemas import PostIn
from app.auth.exceptions import AuthRequired


async def delete_post(session: AsyncSession, post_id: int, token: JWTData):
    post = await session.get(Post, post_id)
    if not post:
        raise PostNotFound()
    if post.user_id != token.user_id:
        raise DeletionRestricted()
    await session.delete(post)
    await session.commit()


async def create_post(session: AsyncSession, request: PostIn, token: JWTData):
    if not token:
        raise AuthRequired()
    new_post = Post(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        user_id=request.user_id,
    )
    session.add(new_post)
    await session.commit()
    await session.refresh(new_post, ["user", "comments"])
    return new_post


async def get_posts(session: AsyncSession):
    return await session.scalars(select(Post).order_by(desc(Post.created_at)))
