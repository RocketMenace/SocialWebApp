from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.posts.models import Post
from app.posts.schemas import PostIn
from app.users.models import User


async def create_post(session: AsyncSession, request: PostIn):
    new_post = Post(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        user_id=request.user_id,
    )
    session.add(new_post)
    await session.commit()
    await session.refresh(new_post, ["user"])
    return new_post


async def get_posts(session: AsyncSession):
    return await session.scalars(select(Post, User).join(Post.user))
