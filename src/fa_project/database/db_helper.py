from collections.abc import AsyncGenerator

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from src.fa_project.settings import settings
from src.fa_project.users.models import User


class DatabaseHelper:
    """Класс для работы с базой данных"""

    def __init__(self, db_url: str, echo: bool) -> None:
        self.engine = create_async_engine(db_url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False
        )

    async def session_dependency(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            try:
                yield session
                await session.commit()
            except SQLAlchemyError as error:
                await session.rollback()
                raise SQLAlchemyError(error)


db_helper = DatabaseHelper(db_url=settings.db_url, echo=settings.DEBUG)
async_session = db_helper.session_dependency


async def get_user_db(session: AsyncSession = Depends(async_session)):
    yield SQLAlchemyUserDatabase(session, User)
