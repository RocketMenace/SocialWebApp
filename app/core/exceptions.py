from typing import Any

from fastapi import HTTPException, status


class DetailedException(HTTPException):
    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR
    DETAIL = "Server error"

    def __init__(self, **kwargs: dict[str, Any]):
        super().__init__(status_code=self.STATUS_CODE, detail=self.DETAIL)


class UnprocessableEntity(DetailedException):
    STATUS_CODE = status.HTTP_422_UNPROCESSABLE_ENTITY


class NotAuthenticated(DetailedException):
    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    DETAIL = "User not authenticated"

    def __init__(self):
        super().__init__(headers={"WWW-Authenticate": "Bearer"})


class BadRequest(DetailedException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
