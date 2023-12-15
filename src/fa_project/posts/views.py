import uuid
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession

from database.db_helper import async_session
from src.fa_project.users.models import User
from src.fa_project.posts import post
from src.fa_project.posts.schemas import PostCreate
from users.dependencises import current_active_user

router = APIRouter(tags=['Посты'], prefix='/posts')

@router.post('/create_post')
async def create_post(post_data: PostCreate, session: Annotated[AsyncSession, Depends(async_session)],
                      user: User = Depends(current_active_user)):
    return await post.create_post(session=session, post_data=post_data, user=user)
