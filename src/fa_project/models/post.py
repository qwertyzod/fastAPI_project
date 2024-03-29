from typing import TYPE_CHECKING

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.fa_project.database.base import Base

if TYPE_CHECKING:
    from models.user import User
    from models.association import Association


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
    association_id: Mapped[int] = mapped_column(ForeignKey(
        'association.id',
        ondelete='CASCADE',
        onupdate='CASCADE',
        name='fk_post_association_id'
    ), nullable=True)
    association: Mapped['Association'] = relationship(back_populates="post", lazy="joined")
