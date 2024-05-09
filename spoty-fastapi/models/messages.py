import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID

metadata = sqlalchemy.MetaData()


messages_table = sqlalchemy.Table(
    "messages",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("album_id", sqlalchemy.Integer),
    sqlalchemy.Column("title", sqlalchemy.String(100)),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime()),
    sqlalchemy.Column("content", sqlalchemy.Text())
)