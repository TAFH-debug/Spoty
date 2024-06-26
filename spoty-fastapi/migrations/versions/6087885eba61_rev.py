"""rev

Revision ID: 6087885eba61
Revises: 175ba1f772a8
Create Date: 2024-05-09 16:25:52.263341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6087885eba61'
down_revision: Union[str, None] = '175ba1f772a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('password', sa.String(), nullable=True))
    op.drop_column('users', 'hashed_password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('users', 'password')
    op.drop_column('messages', 'user_id')
    # ### end Alembic commands ###
