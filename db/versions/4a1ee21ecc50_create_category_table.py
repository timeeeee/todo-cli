"""create category table

Revision ID: 4a1ee21ecc50
Revises: 
Create Date: 2022-12-11 10:01:12.118122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a1ee21ecc50'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "category",
        sa.Column("category_id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String))


def downgrade() -> None:
    op.drop_table("category")
