from fastapi import APIRouter, status
from src.users.schemas import UserResponse, User
from src.users.services import create_user
from src.dependencies import SessionDep

users_router = APIRouter()


@users_router.post(
    path="/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
def user_register(request: User, session: SessionDep):
    return create_user(request, session)
