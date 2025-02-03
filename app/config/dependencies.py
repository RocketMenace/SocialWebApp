from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import database
from typing import Annotated
from fastapi import Depends


SessionDep = Annotated[AsyncSession, Depends(database.get_session)]
