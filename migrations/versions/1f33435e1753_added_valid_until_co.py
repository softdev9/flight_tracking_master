# revision identifiers, used by Alembic.
revision = "1f33435e1753"
down_revision = "ffa5706b1fb"

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column("airports", sa.Column("valid_until", sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("airports", "valid_until")
    ### end Alembic commands ###