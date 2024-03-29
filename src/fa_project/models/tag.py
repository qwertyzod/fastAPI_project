from typing import TYPE_CHECKING

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.fa_project.database.base import Base

if TYPE_CHECKING:
    from models.association import Association


class Tag(Base):
    __tablename__ = 'tag'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    association_id: Mapped[int] = mapped_column(ForeignKey(
        'association.id',
        ondelete='CASCADE',
        onupdate='CASCADE',
        name='fk_tag_association_id'
    ), nullable=True)
    association: Mapped['Association'] = relationship(back_populates="tag", lazy="joined")
