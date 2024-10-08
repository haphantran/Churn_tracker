"""Empty migration

Revision ID: 8e7447b38e11
Revises: a7d65106815d
Create Date: 2024-10-07 21:36:14.337135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e7447b38e11'
down_revision = 'a7d65106815d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('credit_cards', 'user_id', nullable=False)


def downgrade() -> None:
    pass
