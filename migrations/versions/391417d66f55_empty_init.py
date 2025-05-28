"""empty init

Revision ID: 391417d66f55
Revises: 2c5542354c86
Create Date: 2025-05-28 14:12:43.914056

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '391417d66f55'
down_revision: Union[str, None] = '2c5542354c86'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
