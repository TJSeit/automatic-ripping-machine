"""add queue_position to job

Revision ID: a1b2c3d4e5f6
Revises: 95623e8c5d58
Create Date: 2024-10-06 22:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1b2c3d4e5f6'
down_revision = '95623e8c5d58'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('job',
                  sa.Column('queue_position', sa.DateTime())
                  )


def downgrade():
    op.drop_column('job', 'queue_position')
