from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.config.database import database, setup_db
from app.users.router import users_router


@asynccontextmanager
async def lifespan(application: FastAPI):
    await setup_db()
    yield
    await database.close_db()


app = FastAPI(lifespan=lifespan, title="Instagram clone API", root_path="/api")

app.include_router(users_router, prefix="/users", tags=["users"])
