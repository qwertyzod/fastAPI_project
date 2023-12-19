import uuid

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    name: str
    role_id: int | None



class UserUpdate(schemas.BaseUserUpdate):
    pass
