import uuid

from pydantic import BaseModel


class PostRead(BaseModel):
    title: str
    content: str


class PostCreate(BaseModel):
    title: str
    content: str



class PostUpdate(BaseModel):
    title: str
    content: str
