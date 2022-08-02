"""add foreign key to posts table

Revision ID: 696178c745fa
Revises: 9ba79827587e
Create Date: 2022-08-01 17:08:33.621467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '696178c745fa'
down_revision = '9ba79827587e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
                            local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
