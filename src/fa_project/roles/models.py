from typing import TYPE_CHECKING

from sqlalchemy import String, Integer, JSON
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.fa_project.database.base import Base


if TYPE_CHECKING:
    from src.fa_project.users.models import User


class Role(Base):
    __tablename__ = 'role'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    permissions: Mapped[JSON] = mapped_column(JSON)
    user: Mapped[list['User']] = relationship(back_populates="role", lazy="joined")
