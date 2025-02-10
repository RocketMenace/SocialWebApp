from app.core.exceptions import NotFound, Restricted, UnprocessableEntity
from app.posts.constants import ErrorCode


class NotValidData(UnprocessableEntity):
    DETAIL = ErrorCode.NOT_VALID_DATA


class PostNotFound(NotFound):
    DETAIL = ErrorCode.POST_NOT_FOUND


class DeletionRestricted(Restricted):
    DETAIL = ErrorCode.FORBIDDEN
