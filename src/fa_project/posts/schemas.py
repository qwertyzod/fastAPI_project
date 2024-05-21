from pydantic import BaseModel

from tags.schemas import TagCreate


class PostRead(BaseModel):
    id: int
    title: str
    content: str
    image: str


class PostCreate(BaseModel):
    title: str
    content: str
    image: str | None
    tag: TagCreate


class PostUpdate(BaseModel):
    title: str | None
    content: str | None
    image: str | None


class PostDelete(BaseModel):
    id: int
