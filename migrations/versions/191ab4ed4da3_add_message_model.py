"""add message model

Revision ID: 191ab4ed4da3
Revises: d0d980c7f507
Create Date: 2023-04-10 21:07:30.776979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '191ab4ed4da3'
down_revision = 'd0d980c7f507'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('message')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('message', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='message_pkey')
    )
    op.drop_table('messages')
    # ### end Alembic commands ###
