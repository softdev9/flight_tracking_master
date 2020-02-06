# revision identifiers, used by Alembic.
revision = "559cfc0613d2"
down_revision = "2aad9deb5e37"

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "flight_meetings",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("source_id", sa.Integer(), nullable=False),
        sa.Column("destination_id", sa.Integer(), nullable=False),
        sa.Column("start_time", sa.DateTime(), nullable=False),
        sa.Column("end_time", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["destination_id"], ["flights.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["source_id"], ["flights.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "ix_flight_meetings_destination_id",
        "flight_meetings",
        ["destination_id"],
        unique=False,
    )
    op.create_index(
        "ix_flight_meetings_source_id", "flight_meetings", ["source_id"], unique=False
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_flight_meetings_source_id", table_name="flight_meetings")
    op.drop_index("ix_flight_meetings_destination_id", table_name="flight_meetings")
    op.drop_table("flight_meetings")
    ### end Alembic commands ###
