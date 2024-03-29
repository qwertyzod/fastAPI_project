from typing import TYPE_CHECKING

from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.fa_project.database.base import Base

if TYPE_CHECKING:
    from models.user import User


class Role(Base):
    __tablename__ = 'role'
    __table_args__ = {'extend_existing': True}
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    permissions: Mapped[int] = mapped_column(Integer)
    user: Mapped[list['User']] = relationship(back_populates="role", lazy="joined")
