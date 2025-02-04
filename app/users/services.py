from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.security import hash_password
from app.users.models import User
from app.users.schemas import UserIn


async def create_user(session: AsyncSession, request: UserIn):
    new_user = User(
        username=request.username,
        email=request.email,
        password=hash_password(request.password),
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user
