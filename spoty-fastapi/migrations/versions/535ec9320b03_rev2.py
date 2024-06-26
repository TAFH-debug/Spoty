"""rev2

Revision ID: 535ec9320b03
Revises: 6087885eba61
Create Date: 2024-05-09 17:59:31.005998

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '535ec9320b03'
down_revision: Union[str, None] = '6087885eba61'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('username', sa.String(length=100), nullable=True))
    op.drop_column('messages', 'title')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('title', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_column('messages', 'username')
    # ### end Alembic commands ###
