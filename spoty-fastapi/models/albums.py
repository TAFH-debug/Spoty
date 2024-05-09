import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID

metadata = sqlalchemy.MetaData()


albums_table = sqlalchemy.Table(
    "albums",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(100)),
    sqlalchemy.Column("author", sqlalchemy.String(100)),
    sqlalchemy.Column("genre", sqlalchemy.String(100)),
    sqlalchemy.Column("description", sqlalchemy.Text()),
    sqlalchemy.Column("image", sqlalchemy.String(100)),
)