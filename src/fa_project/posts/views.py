from typing import Annotated

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from database.db_helper import async_session
from src.fa_project.models import User
from src.fa_project.posts import post
from src.fa_project.posts.schemas import PostCreate, PostUpdate
from users.dependencises import current_active_user


router = APIRouter(tags=['Посты'], prefix='/posts')


@router.post('')
async def create_post(
        post_data: PostCreate,
        session: Annotated[AsyncSession, Depends(async_session)],
        user: User = Depends(current_active_user)
):
    return await post.create_post(session=session, post_data=post_data, user=user)


@router.patch('')
async def update_post(
        post_id: int,
        post_data: PostUpdate,
        session: Annotated[AsyncSession, Depends(async_session)],
):
    return await post.update_post(session=session, post_id=post_id, post_data=post_data)


@router.get('/get_personal_posts')
async def get_posts_user(user: User = Depends(current_active_user)):
    return await post.get_posts(user=user)


@router.get('')
async def get_all_posts(session: Annotated[AsyncSession, Depends(async_session)]):
    return await post.get_all_posts(session=session)


@router.delete('/delete_post')
async def delete_post(post_id: int, session: Annotated[AsyncSession, Depends(async_session)]):
    return await post.delete_post(post_id=post_id, session=session)
