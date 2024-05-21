from typing import TYPE_CHECKING

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.fa_project.database.base import Base
from src.fa_project.models.association import association_table

if TYPE_CHECKING:
    from .user import User

    from .tag import Tag


class Post(Base):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    image: Mapped[str] = mapped_column(String)

    user_id: Mapped[int] = mapped_column(ForeignKey(
        'user.id',
        ondelete='CASCADE',
        onupdate='CASCADE',
        name='fk_post_user_id'
    ), nullable=True)
    user: Mapped['User'] = relationship(back_populates="post", lazy="joined")
    tag: Mapped[list['Tag']] = relationship(
        secondary=association_table,
        back_populates="post",
    )
