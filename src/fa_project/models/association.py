from sqlalchemy import Column, ForeignKey, Table, Integer, UniqueConstraint

from src.fa_project.database.base import Base

association_table = Table(
    'association',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('post_id', ForeignKey('post.id'), nullable=False),
    Column('tag_id', ForeignKey('tag.id'), nullable=False),
    UniqueConstraint('post_id', 'tag_id', name='unique_post_tag'),
)
