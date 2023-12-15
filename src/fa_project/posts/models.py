import uuid
from typing import TYPE_CHECKING

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.fa_project.database.base import Base

if TYPE_CHECKING:
    from src.fa_project.users.models import User

class Post(Base):
    __tablename__ = "post"
    __table_args__ = {'extend_existing': True}
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    image: Mapped[str] = mapped_column(String)

    user: Mapped[list['User']] = relationship(back_populates="post", lazy="joined")
