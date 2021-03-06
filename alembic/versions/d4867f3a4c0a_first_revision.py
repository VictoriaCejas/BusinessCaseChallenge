"""First revision

Revision ID: d4867f3a4c0a
Revises:
Create Date: 2019-04-17 13:53:32.978401

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "d4867f3a4c0a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "business",
        sa.Column("company_id", sa.Integer(), nullable=False, autoincrement=True),
        sa.Column("name", sa.String()),
        sa.Column("link", sa.String()),
        sa.Column("date_added", sa.Date()),
        sa.Column("contact_first_name", sa.String()),
        sa.Column("contact_last_name", sa.String()),
        sa.Column("contact_phone_number", sa.String()),
        sa.Column("contact_email", sa.String()),
        sa.Column("country", sa.String()),
        sa.PrimaryKeyConstraint("company_id"),
    )

    op.create_table(
        "vacancy",
        sa.Column("vacancy_id", sa.Integer(), nullable=False, autoincrement=True),
        sa.Column("salary", sa.Float()),
        sa.Column("max_experience", sa.Integer()),
        sa.Column("min_experience", sa.Integer()),
        sa.Column("vacancy_link", sa.String()),
        sa.Column("skills", sa.Text()),
        sa.Column("position_name", sa.String()),
        sa.Column("active", sa.Boolean()),
        sa.Column("company_id", sa.Integer()),
        sa.ForeignKeyConstraint(["company_id"], ["business.company_id"],),
        sa.PrimaryKeyConstraint("vacancy_id"),
    )

    # ### end Alembic commands ###

    def downgrade():
        # ### commands auto generated by Alembic - please adjust! ###
        op.drop_table("business")
        op.drop_table("vacancy")
        # ### end Alembic commands ###
