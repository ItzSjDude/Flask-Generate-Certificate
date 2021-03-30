"""empty message

Revision ID: 77094592831e
Revises: 1d0d4b07df15
Create Date: 2021-03-29 16:05:40.868253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77094592831e'
down_revision = '1d0d4b07df15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('token_id', sa.String(length=200), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('sqlite_stat1')
    op.drop_table('sqlite_stat4')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sqlite_stat4',
    sa.Column('tbl', sa.NullType(), nullable=True),
    sa.Column('idx', sa.NullType(), nullable=True),
    sa.Column('neq', sa.NullType(), nullable=True),
    sa.Column('nlt', sa.NullType(), nullable=True),
    sa.Column('ndlt', sa.NullType(), nullable=True),
    sa.Column('sample', sa.NullType(), nullable=True)
    )
    op.create_table('sqlite_stat1',
    sa.Column('tbl', sa.NullType(), nullable=True),
    sa.Column('idx', sa.NullType(), nullable=True),
    sa.Column('stat', sa.NullType(), nullable=True)
    )
    op.drop_table('token')
    # ### end Alembic commands ###
