from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database import database


class Post(database.Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship("User", back_populates="posts")
    image_url: Mapped[str]
    image_url_type: Mapped[str]
    caption: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=func.now())
