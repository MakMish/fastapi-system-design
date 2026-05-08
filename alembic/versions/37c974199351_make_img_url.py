"""make img-url

Revision ID: 37c974199351
Revises: 
Create Date: 2026-05-05 12:10:38.297373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37c974199351'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column(
        "user_table",
        sa.Column("img_url", sa.String(length=500))
    )


def downgrade():
    op.drop_column("user_table", "img_url")
