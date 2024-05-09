import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID

metadata = sqlalchemy.MetaData()


reviews_table = sqlalchemy.Table(
    "reviews",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("album_id", sqlalchemy.Integer),
    sqlalchemy.Column("username", sqlalchemy.String(100)),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime()),
    sqlalchemy.Column("content", sqlalchemy.Text()),
    sqlalchemy.Column("user_id", sqlalchemy.Integer),
    sqlalchemy.Column("score", sqlalchemy.Integer)
)