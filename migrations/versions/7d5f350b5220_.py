"""empty message

Revision ID: 7d5f350b5220
Revises: 2e715bf6ba63
Create Date: 2022-08-25 20:01:16.147068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d5f350b5220'
down_revision = '2e715bf6ba63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_final',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('blog_posts_final',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=250), nullable=False),
    sa.Column('subtitle', sa.String(length=250), nullable=False),
    sa.Column('date', sa.String(length=1000), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('img_url', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user_final.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.drop_table('blog_posts')
    op.drop_table('blog_user')
    op.add_column('comments', sa.Column('commenter_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('comment_of_post', sa.Integer(), nullable=True))
    op.drop_constraint('comments_post_id_fkey', 'comments', type_='foreignkey')
    op.drop_constraint('comments_comment_author_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'user_final', ['commenter_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'blog_posts_final', ['comment_of_post'], ['id'])
    op.drop_column('comments', 'comment_author_id')
    op.drop_column('comments', 'post_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('comments', sa.Column('comment_author_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_comment_author_id_fkey', 'comments', 'blog_user', ['comment_author_id'], ['id'])
    op.create_foreign_key('comments_post_id_fkey', 'comments', 'blog_posts', ['post_id'], ['id'])
    op.drop_column('comments', 'comment_of_post')
    op.drop_column('comments', 'commenter_id')
    op.create_table('blog_user',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('blog_user_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=1000), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='blog_user_pkey'),
    sa.UniqueConstraint('email', name='blog_user_email_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('blog_posts',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('subtitle', sa.VARCHAR(length=450), autoincrement=False, nullable=False),
    sa.Column('date', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('body', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('img_url', sa.VARCHAR(length=1000), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['blog_user.id'], name='blog_posts_author_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='blog_posts_pkey'),
    sa.UniqueConstraint('title', name='blog_posts_title_key')
    )
    op.drop_table('blog_posts_final')
    op.drop_table('user_final')
    # ### end Alembic commands ###
