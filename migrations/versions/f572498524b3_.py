"""empty message

Revision ID: f572498524b3
Revises: 79b00b332234
Create Date: 2024-07-15 09:27:41.501282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f572498524b3'
down_revision = '79b00b332234'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parcel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pickup_location', sa.String(), nullable=True),
    sa.Column('destination', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profile_picture', sa.String(length=255), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_parcel_association',
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('parcel_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['orders.order_id'], ),
    sa.ForeignKeyConstraint(['parcel_id'], ['parcel.id'], )
    )
    op.drop_table('items')
    op.drop_table('order_item')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=60),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=110),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=40),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=40),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=110),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.String(length=60),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)

    op.create_table('order_item',
    sa.Column('order_id', sa.INTEGER(), nullable=False),
    sa.Column('item_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['orders.order_id'], ),
    sa.PrimaryKeyConstraint('order_id', 'item_id')
    )
    op.create_table('items',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('item_name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=False),
    sa.Column('price', sa.INTEGER(), nullable=False),
    sa.Column('order_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.order_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('order_parcel_association')
    op.drop_table('profiles')
    op.drop_table('parcel')
    # ### end Alembic commands ###