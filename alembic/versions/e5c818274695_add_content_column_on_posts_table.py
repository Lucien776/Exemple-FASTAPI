"""Add content column on posts table

Revision ID: e5c818274695
Revises: ac77cc307b3d
Create Date: 2022-01-15 12:16:12.741808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5c818274695'
down_revision = 'ac77cc307b3d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
