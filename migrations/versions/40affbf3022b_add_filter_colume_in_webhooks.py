"""add filter colume in webhooks

Revision ID: 40affbf3022b
Revises: 5d5f801f28e7
Create Date: 2023-08-28 12:30:35.171176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40affbf3022b'
down_revision = '5d5f801f28e7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('webhooks', sa.Column('filters', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('webhooks', 'filters')
    # ### end Alembic commands ###
