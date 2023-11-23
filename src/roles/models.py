from typing import TYPE_CHECKING

from sqlalchemy import String, Integer, JSON, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.base import Base


if TYPE_CHECKING:
    from src.users.models import User

class Role(Base):
    __tablename__ = 'role'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100), nullable=False)
    permissions = mapped_column(JSON)
    user: Mapped[list['User']] = relationship(back_populates="role", lazy="joined")
