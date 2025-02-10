from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict

from app.comments.schemas import Comment
from app.users.schemas import User


class BasePost(BaseModel):
    image_url: str
    image_url_type: Literal["absolute", "relative"]
    caption: str
    user_id: int


class PostIn(BasePost):
    pass


class Post(BasePost):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime
    user: User
    comments: list[Comment]
