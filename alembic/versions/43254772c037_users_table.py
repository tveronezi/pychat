"""users table

Revision ID: 43254772c037
Revises: ed2d6d932904
Create Date: 2022-06-26 20:56:25.996683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "43254772c037"
down_revision = "ed2d6d932904"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("uuid", sa.dialects.postgresql.UUID, primary_key=True),
        sa.Column("name", sa.Text),
    )
    op.create_foreign_key(
        constraint_name="messages_users_from_fk",
        source_table="messages",
        referent_table="users",
        local_cols=["from"],
        remote_cols=["uuid"],
    )
    op.create_foreign_key(
        constraint_name="messages_users_to_fk",
        source_table="messages",
        referent_table="users",
        local_cols=["to"],
        remote_cols=["uuid"],
    )


def downgrade() -> None:
    op.drop_constraint("messages_users_from_fk", "messages", type_="foreignkey")
    op.drop_constraint("messages_users_to_fk", "messages", type_="foreignkey")
    op.drop_table("users")
