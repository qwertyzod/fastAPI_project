"""Add post model

Revision ID: 1b2c1d993285
Revises: e3ef1ff64828
Create Date: 2023-12-08 11:57:56.670412

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from src.fa_project import Base

# revision identifiers, used by Alembic.
revision: str = '1b2c1d993285'
down_revision: Union[str, None] = 'e3ef1ff64828'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('post_id', sa.Integer(), nullable=False))
    op.create_foreign_key('fk_user_post_id', 'user', 'posts', ['post_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')

    role = Base.metadata.tables['role']
    # ### end Alembic commands ###
    op.bulk_insert(role, [
        {'id': 1, 'name': 'admin', 'permissions': 1},
        {'id': 2, 'name': 'user', 'permissions': 0}
    ])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_user_post_id', 'user', type_='foreignkey')
    op.drop_column('user', 'post_id')
    op.drop_table('posts')
    # ### end Alembic commands ###
