from sqlalchemy.orm import Session
from sqlalchemy import select
from src.users.schemas import User
from src.users.models import User
from src.auth.security import hash_password


def create_user(request: User, session: Session) -> User:
    new_user = User(
        username=request.username,
        email=request.email,
        password=hash_password(request.password),
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user
