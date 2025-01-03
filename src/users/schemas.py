from pydantic import BaseModel


class BaseUser(BaseModel):
    username: str
    email: str


class User(BaseUser):
    password: str


class UserResponse(BaseUser):
    id: int

    class Config:
        from_attributes = True
