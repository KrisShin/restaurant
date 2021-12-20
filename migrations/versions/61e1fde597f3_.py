"""empty message

Revision ID: 61e1fde597f3
Revises: d6e78881bfa8
Create Date: 2021-11-28 22:45:16.790753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61e1fde597f3'
down_revision = 'd6e78881bfa8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_comment', sa.Column('rate', sa.Enum('good', 'normal', 'bad', name='rate_enum'), nullable=True))
    op.add_column('tb_user', sa.Column('role', sa.Enum('user', 'admin', name='role_enum'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tb_user', 'role')
    op.drop_column('tb_comment', 'rate')
    # ### end Alembic commands ###
