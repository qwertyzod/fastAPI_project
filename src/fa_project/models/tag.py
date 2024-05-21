from typing import TYPE_CHECKING

from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.fa_project.database.base import Base
from src.fa_project.models.association import association_table

if TYPE_CHECKING:
    from .post import Post


class Tag(Base):
    __tablename__ = 'tag'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    post: Mapped[list['Post']] = relationship(
        secondary=association_table,
        back_populates="tag",
    )
