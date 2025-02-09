from app.auth.constants import ErrorCode
from app.core.exceptions import BadRequest, NotAuthenticated


class InvalidCredentials(BadRequest):
    DETAIL = "Invalid credentials"


class InvalidToken(NotAuthenticated):
    DETAIL = ErrorCode.INVALID_TOKEN
