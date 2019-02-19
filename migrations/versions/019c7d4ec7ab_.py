"""empty message

Revision ID: 019c7d4ec7ab
Revises: 
Create Date: 2019-02-19 11:04:20.084840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '019c7d4ec7ab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meetings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Text(), nullable=True),
    sa.Column('meeting_time', sa.Text(), nullable=True),
    sa.Column('attended', sa.Text(), nullable=True),
    sa.Column('topics', sa.Text(), nullable=True),
    sa.Column('todo', sa.Text(), nullable=True),
    sa.Column('completed', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('meetings')
    # ### end Alembic commands ###
