from fastapi import APIRouter, status

from app.config.dependencies import SessionDep
from app.users.schemas import User, UserIn
from app.users.services import create_user

users_router = APIRouter()


@users_router.post(
    path="/register", response_model=User, status_code=status.HTTP_201_CREATED
)
async def user_register(request: UserIn, session: SessionDep):
    return await create_user(session, request)
