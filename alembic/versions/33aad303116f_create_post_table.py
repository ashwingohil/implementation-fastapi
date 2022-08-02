"""create post table

Revision ID: 33aad303116f
Revises: 
Create Date: 2022-08-01 15:52:23.922610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33aad303116f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True)
                    , sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
