"""add content column to posts table

Revision ID: 9aa62a47de37
Revises: 33aad303116f
Create Date: 2022-08-01 16:54:27.750335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9aa62a47de37'
down_revision = '33aad303116f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
