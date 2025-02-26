from pydantic import BaseModel, Field


class JWTData(BaseModel):
    user_id: int
    email: str = Field(alias="sub")


class AuthUser(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
