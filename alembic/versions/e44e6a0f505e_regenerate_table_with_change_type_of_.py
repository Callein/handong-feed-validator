"""Regenerate table with change type of TbKaMessage.message String(500) to Text - TbSubject, TbKaMessage

Revision ID: e44e6a0f505e
Revises: a9acae6fee20
Create Date: 2024-09-14 21:49:06.044942

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'e44e6a0f505e'
down_revision: Union[str, None] = 'a9acae6fee20'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('TbKaMessage',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('chat_id', sa.BigInteger(), nullable=False),
    sa.Column('client_message_id', sa.BigInteger(), nullable=False),
    sa.Column('room_id', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('message', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('last_sent_at', sa.Integer(), nullable=True),
    sa.Column('deleted', sa.String(length=1), nullable=True),
    sa.Column('subject_id', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('TbSubject',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('last_sent_at', sa.Integer(), nullable=True),
    sa.Column('last_sent_chat_id', sa.BigInteger(), nullable=True),
    sa.Column('deleted', sa.String(length=1), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('TbSubject')
    op.drop_table('TbKaMessage')
    # ### end Alembic commands ###
