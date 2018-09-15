"""initial migration

Revision ID: 1aa5bf186669
Revises: 456a945560f6
Create Date: 2018-08-01 23:41:17.031292

"""

# revision identifiers, used by Alembic.
revision = '1aa5bf186669'
down_revision = '456a945560f6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('strategies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('strategyname', sa.String(length=64), nullable=True),
    sa.Column('code', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_strategies_strategyname'), 'strategies', ['strategyname'], unique=True)
    op.create_index(op.f('ix_strategies_timestamp'), 'strategies', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_strategies_timestamp'), table_name='strategies')
    op.drop_index(op.f('ix_strategies_strategyname'), table_name='strategies')
    op.drop_table('strategies')
    # ### end Alembic commands ###