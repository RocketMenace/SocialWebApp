from typing import Annotated

from fastapi import Depends

from src.database import SessionLocal


def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SessionDep = Annotated[SessionLocal, Depends(get_session)]
