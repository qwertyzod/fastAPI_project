import uuid

from pydantic import BaseModel


class PostRead(BaseModel):
    id: int
    title: str
    content: str
    image: str
    user_name: uuid.UUID


class PostCreate(BaseModel):
    title: str
    content: str
    image: str | None


class PostUpdate(BaseModel):
    title: str | None
    content: str | None
    image: str | None


class PostDelete(BaseModel):
    id: int
