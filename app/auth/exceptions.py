from app.core.exceptions import NotAuthenticated, BadRequest
from app.auth.constants import ErrorCode


class EmailTaken(BadRequest):
    DETAIL = ErrorCode.EMAIL_TAKEN


class InvalidCredentials(BadRequest):
    DETAIL = "Invalid credentials"


class InvalidToken(NotAuthenticated):
    DETAIL = ErrorCode.INVALID_TOKEN
