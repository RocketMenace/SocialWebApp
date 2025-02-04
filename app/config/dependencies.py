from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import database

SessionDep = Annotated[AsyncSession, Depends(database.get_session)]
