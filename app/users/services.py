import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.security import hash_password
from app.users.exceptions import EmailTaken
from app.users.models import User
from app.users.schemas import UserIn


async def get_user_by_email(session: AsyncSession, email: str):
    return await session.scalar(select(User).where(User.email == email))


async def create_user(session: AsyncSession, request: UserIn):
    if await get_user_by_email(session, request.email):
        raise EmailTaken
    new_user = User(
        username=request.username,
        email=request.email,
        password=await asyncio.to_thread(hash_password, request.password),
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user
