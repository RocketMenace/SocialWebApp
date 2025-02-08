from fastapi.security import OAuth2PasswordBearer
from app.config.config import config
from app.users.models import User
from app.users.schemas import UserIn
from datetime import timedelta, datetime, timezone
import jwt
from fastapi import Depends
from app.auth.schemas import JWTData
from app.auth.exceptions import InvalidToken


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
SECRET_KEY = config.API_KEY
JWT_ALGORITHM = config.JWT_ALGORITHM


def create_access_token(user_data: User) -> str:
    expire_delta = timedelta(minutes=config.JWT_EXPIRED)
    jwt_data = {
        "sub": user_data.email,
        "exp": datetime.now(tz=timezone.utc) + expire_delta,
    }
    return jwt.encode(jwt_data, key=SECRET_KEY, algorithm=JWT_ALGORITHM)


def decode_token(token: str = Depends(oauth2_scheme)) -> JWTData | None:
    if not token:
        return None

    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=[JWT_ALGORITHM])
    except jwt.PyJWTError:
        raise InvalidToken()
    return JWTData(**payload)
