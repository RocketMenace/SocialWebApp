from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.auth.router import auth_router
from app.comments.router import comments_router
from app.config.database import database, setup_db
from app.files.router import files_router
from app.posts.router import posts_router
from app.users.router import users_router


@asynccontextmanager
async def lifespan(application: FastAPI):
    await setup_db()
    yield
    await database.close_db()


app = FastAPI(lifespan=lifespan, title="Instagram clone API", root_path="/api")

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(posts_router, prefix="/posts", tags=["posts"])
app.include_router(files_router, prefix="/files", tags=["files"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(comments_router, prefix="/comments", tags=["posts", "comments"])
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
