from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import engine, SessionLocal
from typing import Annotated


def get_session():
    with SessionLocal as session:
        yield session

SessionDep = Annotated[AsyncSession, get_session()]