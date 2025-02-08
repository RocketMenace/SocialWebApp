from pydantic import BaseModel, ConfigDict, Field


class UserBase(BaseModel):
    username: str
    email: str


class UserIn(UserBase):
    password: str


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    pass
