from app.core.exceptions import UnprocessableEntity
from app.posts.constants import ErrorCode


class NotValidData(UnprocessableEntity):
    DETAIL = ErrorCode.NOT_VALID_DATA
