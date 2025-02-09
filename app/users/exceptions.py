from app.core.exceptions import BadRequest
from app.users.constants import ErrorCode


class EmailTaken(BadRequest):
    DETAIL = ErrorCode.EMAIL_TAKEN
