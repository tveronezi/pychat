"""messages table

Revision ID: ed2d6d932904
Revises: 
Create Date: 2022-06-26 20:30:19.921400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ed2d6d932904"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "messages",
        sa.Column("uuid", sa.dialects.postgresql.UUID, primary_key=True),
        sa.Column("from", sa.dialects.postgresql.UUID, nullable=False),
        sa.Column("to", sa.dialects.postgresql.UUID, nullable=False),
        sa.Column("content", sa.Text),
    )


def downgrade() -> None:
    op.drop_table("messages")
