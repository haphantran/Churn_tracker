"""Initial migration

Revision ID: d5ad9ca72018
Revises: 
Create Date: 2024-10-06 23:29:13.457976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5ad9ca72018'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bonuses', 'id',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('bonuses', 'credit_card_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('bonuses', 'bonus_type',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('bonuses', 'points',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('bonuses', 'amount_spending_required',
               existing_type=sa.REAL(),
               nullable=True)
    op.alter_column('bonuses', 'deadline',
               existing_type=sa.DATE(),
               nullable=True)
    op.create_index(op.f('ix_bonuses_id'), 'bonuses', ['id'], unique=False)
    op.alter_column('credit_cards', 'id',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('credit_cards', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('credit_cards', 'card_name',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('credit_cards', 'card_holder',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('credit_cards', 'welcome_bonus',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('credit_cards', 'welcome_spending_amount',
               existing_type=sa.REAL(),
               nullable=True)
    op.alter_column('credit_cards', 'welcome_spending_deadline',
               existing_type=sa.DATE(),
               nullable=True)
    op.create_index(op.f('ix_credit_cards_id'), 'credit_cards', ['id'], unique=False)
    op.alter_column('users', 'id',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('users', 'email',
               existing_type=sa.TEXT(),
               nullable=True)
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.alter_column('users', 'email',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('users', 'id',
               existing_type=sa.INTEGER(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
               existing_nullable=False,
               autoincrement=True)
    op.drop_index(op.f('ix_credit_cards_id'), table_name='credit_cards')
    op.alter_column('credit_cards', 'welcome_spending_deadline',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('credit_cards', 'welcome_spending_amount',
               existing_type=sa.REAL(),
               nullable=False)
    op.alter_column('credit_cards', 'welcome_bonus',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('credit_cards', 'card_holder',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('credit_cards', 'card_name',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('credit_cards', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('credit_cards', 'id',
               existing_type=sa.INTEGER(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
               existing_nullable=False,
               autoincrement=True)
    op.drop_index(op.f('ix_bonuses_id'), table_name='bonuses')
    op.alter_column('bonuses', 'deadline',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('bonuses', 'amount_spending_required',
               existing_type=sa.REAL(),
               nullable=False)
    op.alter_column('bonuses', 'points',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('bonuses', 'bonus_type',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('bonuses', 'credit_card_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('bonuses', 'id',
               existing_type=sa.INTEGER(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
               existing_nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###
