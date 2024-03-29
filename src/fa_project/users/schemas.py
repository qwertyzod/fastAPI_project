import uuid
from typing import List
from fastapi_users import schemas
from pydantic import BaseModel

from src.fa_project.posts.schemas import PostRead


class UserRead(BaseModel):
    email: str
    id: uuid.UUID
    name: str
    role_id: int
    post: List[PostRead]


class UserCreate(schemas.BaseUserCreate):
    name: str
    role_id: int | None


class UserUpdate(schemas.BaseUserUpdate):
    name: str
