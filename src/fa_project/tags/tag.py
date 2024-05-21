from sqlalchemy.ext.asyncio import AsyncSession

from src.fa_project.models import Tag


async def create_tag(session: AsyncSession, tag_name: str):
    tag = Tag(name=tag_name)
    session.add(tag)
    await session.commit()
    return tag
