from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CommentBase(BaseModel):
    username: str
    text: str
    post_id: int


class CommentIn(CommentBase):
    pass


class Comment(CommentBase):
    model_config = ConfigDict(from_attributes=True)
    created_at: datetime
