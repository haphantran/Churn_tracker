"""upgrade users to add password field

Revision ID: a1b49201d4fc
Revises: 8e7447b38e11
Create Date: 2024-10-07 22:59:02.690361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1b49201d4fc'
down_revision = '8e7447b38e11'
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
