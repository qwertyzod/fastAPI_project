import uuid
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin, schemas, models, exceptions

from src.fa_project.users.models import User
from database.db_helper import get_user_db
from settings import settings


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = settings.SECRET
    verification_token_secret = settings.SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def create(self, user_create: schemas.UC, safe: bool = False, request: Optional[Request] = None):
        user_create.update(role_id = 2)
        return await super().create(user_create, safe, request)



async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
