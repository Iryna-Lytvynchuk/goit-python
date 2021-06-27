"""create account table

Revision ID: 975367907b7e
Revises: 
Create Date: 2021-06-27 22:06:04.502119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '975367907b7e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('surname', sa.String(50), nullable=False),
        sa.Column('adress', sa.String(50), nullable=False),
        sa.Column('note', sa.String(50), nullable=False),
        sa.Column('tag', sa.String(50), nullable=False),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('phone', sa.Integer, nullable=False),
        sa.Column('birthday', sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table('users')
