from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.fa_project.models import Post
from src.fa_project.models import User, Tag
from src.fa_project.posts.schemas import PostCreate, PostUpdate

from tags.tag import create_tag


async def create_post(session: AsyncSession, post_data: PostCreate, user: User) -> None:
    try:
        existing_tag = await session.execute(select(Tag).filter(Tag.name == post_data.tag.name))
        existing_tag = existing_tag.scalar_one_or_none()
        if existing_tag is None:
            tag = await create_tag(session=session, tag_name=post_data.tag.name)
        else:
            tag = existing_tag
        post = Post(title=post_data.title, content=post_data.content, image=post_data.image, tag=[tag])
        post.user_id = user.id
        session.add(post)
        await session.commit()
    except Exception:
        await session.rollback()


async def get_posts(user: User) -> List[Post]:
    return await user.post


async def get_all_posts(session: AsyncSession) -> List[Post]:
    query = select(Post)
    result = await session.execute(query)
    return list(result.unique().scalars().all())


async def delete_post(post_id: int, session: AsyncSession) -> dict:
    stmt = delete(Post).where(Post.id == post_id)
    await session.execute(stmt)
    return {"message": "Post deleted"}


async def update_post(session: AsyncSession, post_id: int, post_data: PostUpdate) -> Post:
    data = {key: value for key, value in post_data.model_dump().items() if value is not None}
    stmt = update(Post).where(Post.id == post_id).values(**data)
    await session.execute(stmt)
    query = select(Post).filter(Post.id == post_id)
    post = await session.scalar(query)
    return post
