from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.exceptions import InvalidCredentials
from app.auth.schemas import AuthUser
from app.auth.security import verify_password
from app.users.services import get_user_by_email


async def authenticate_user(session: AsyncSession, user_data: AuthUser):
    user = await get_user_by_email(session, user_data.email)
    if not user:
        raise InvalidCredentials()
    if not verify_password(user_data.password, user.password):
        raise InvalidCredentials()
    return user
