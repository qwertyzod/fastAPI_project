from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.fa_project.database.base import Base


class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    image: Mapped[str] = mapped_column(String)
    user: Mapped[list['User']] = relationship(back_populates="post", lazy="joined")
