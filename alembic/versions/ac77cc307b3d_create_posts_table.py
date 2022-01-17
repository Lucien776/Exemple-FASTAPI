"""create posts table

Revision ID: ac77cc307b3d
Revises: 
Create Date: 2022-01-15 11:30:11.536282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac77cc307b3d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
