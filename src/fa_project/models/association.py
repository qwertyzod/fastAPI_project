from typing import TYPE_CHECKING

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.fa_project.database.base import Base

if TYPE_CHECKING:
    from models.tag import Tag
    from models.post import Post


class Association(Base):
    __tablename__ = 'association'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    post: Mapped['Post'] = relationship(back_populates="post", lazy="joined")
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'))
    tag: Mapped['Tag'] = relationship(back_populates="tag", lazy="joined")
    tag_id: Mapped[int] = mapped_column(ForeignKey('tag.id'))
