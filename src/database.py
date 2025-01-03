from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from src.config import settings

SQL_ALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database URL is ", SQL_ALCHEMY_DATABASE_URL)
engine = create_engine(SQL_ALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass
