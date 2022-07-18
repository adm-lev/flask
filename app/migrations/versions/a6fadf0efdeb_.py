"""empty message

Revision ID: a6fadf0efdeb
Revises: 0eed1730f6d4
Create Date: 2022-07-18 13:44:16.164021

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a6fadf0efdeb'
down_revision = '0eed1730f6d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('slug', table_name='post')
    op.drop_table('post')
    op.drop_table('tag')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('slug', mysql.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('post',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=140), nullable=True),
    sa.Column('slug', mysql.VARCHAR(length=140), nullable=True),
    sa.Column('body', mysql.TEXT(), nullable=True),
    sa.Column('created', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('slug', 'post', ['slug'], unique=False)
    # ### end Alembic commands ###