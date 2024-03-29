
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.fa_project.posts.models import Post
from src.fa_project.users.models import User
from src.fa_project.posts.schemas import PostCreate


async def create_post(session: AsyncSession, post_data: PostCreate, user: User) -> dict:
    post = Post(**post_data.model_dump())
    post.user_id = user.id
    post_create = {key: value for key, value in vars(post).items() if not key.startswith('_')}
    stmt = insert(Post).values(post_create)
    await session.execute(stmt)
    return {"message": "Post created"}


async def get_posts(user: User):
    return user.post


async def get_all_posts(session: AsyncSession):
    query = select(Post)
    result = await session.execute(query)
    return result.unique().scalars().all()


async def delete_post(post_id: int, session: AsyncSession):
    stmt = delete(Post).where(Post.id == post_id)
    await session.execute(stmt)
    return {"message": "Post deleted"}
