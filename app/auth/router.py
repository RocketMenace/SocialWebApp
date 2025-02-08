from fastapi import APIRouter, status
from app.auth.schemas import AuthUser, TokenResponse
from app.config.dependencies import SessionDep
from app.auth.services import authenticate_user
from app.auth.jwt import create_access_token

auth_router = APIRouter()


@auth_router.post(path="/login", status_code=status.HTTP_200_OK)
async def login(request: AuthUser, session: SessionDep):
    user = await authenticate_user(session, user_data=request)
    token= create_access_token(user)
    return TokenResponse(access_token=token)

