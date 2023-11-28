import uuid

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    role_id: int


class UserCreate(schemas.BaseUserCreate):
    role_id: int


class UserUpdate(schemas.BaseUserUpdate):
    pass