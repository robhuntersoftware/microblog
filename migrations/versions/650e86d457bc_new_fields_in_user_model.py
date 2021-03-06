"""new fields in user model

Revision ID: 650e86d457bc
Revises: 6f32602a2f53
Create Date: 2018-03-15 16:49:47.363159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '650e86d457bc'
down_revision = '6f32602a2f53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
