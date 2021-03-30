"""empty message

Revision ID: fca98213172f
Revises: 77094592831e
Create Date: 2021-03-29 16:08:45.856393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fca98213172f'
down_revision = '77094592831e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    # ### end Alembic commands ###
