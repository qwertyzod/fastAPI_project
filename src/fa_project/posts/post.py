import uuid
from datetime import datetime
from typing import Union

from fastapi import HTTPException, status
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.fa_project.posts.models import Post
from src.fa_project.users.models import User
from src.fa_project.posts.schemas import PostCreate


async def create_post(session: AsyncSession, post_data: PostCreate, user: User) -> Post:
    post = Post(**post_data.model_dump())
    post.user_id = user.id
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post
