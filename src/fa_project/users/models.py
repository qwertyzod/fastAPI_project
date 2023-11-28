from datetime import datetime
from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from fa_project.database.base import Base

if TYPE_CHECKING:
    from fa_project.roles.models import Role

class User(SQLAlchemyBaseUserTableUUID, Base):
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    role: Mapped['Role'] = relationship(back_populates="user", lazy="joined")
    role_id: Mapped[int] = mapped_column(ForeignKey('role.id', ondelete='CASCADE', onupdate='CASCADE'))
