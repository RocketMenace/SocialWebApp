from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database import database
from app.posts.models import Post


class User(database.Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    username: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    posts = relationship(
        "Post", back_populates="user", cascade="all, delete", order_by="Post.created_at"
    )
    password: Mapped[str]
