from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select, desc, insert
import datetime
from pydantic import BaseModel
from os import environ
from models.messages import messages_table
from models.users import users_table
import databases

DB_USER = environ.get("DB_USER", "postgres")
DB_PASSWORD = environ.get("DB_PASSWORD", "postgres")
DB_HOST = environ.get("DB_HOST", "localhost")
DB_NAME = "postgres"
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)

database = databases.Database(SQLALCHEMY_DATABASE_URL)

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AlbumId(BaseModel):
    album_id: int
    

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    
@app.get("/api/trends")
async def trends():
    return {"message": "Hello World"}

@app.post("/api/get_all_messages")
async def get_messages(body: AlbumId):
    query = (
        select(
            messages_table.c.id,
            messages_table.c.album_id,
            messages_table.c.title,
            messages_table.c.created_at,
            messages_table.c.content
        )
        .order_by(desc(messages_table.c.created_at))
        
    )
    return await database.fetch_all(query)

@app.post("/api/get_messages")
async def get_messages(body: AlbumId):
    query = (
        select(
            messages_table.c.id,
            messages_table.c.album_id,
            messages_table.c.title,
            messages_table.c.created_at,
            messages_table.c.content
        )
        .where(messages_table.c.album_id == body.album_id)
        .order_by(desc(messages_table.c.created_at))
        
    )
    return await database.fetch_all(query)

@app.get("/api/create_message")
async def message(data = Body()):
    query = (
        insert(
            messages_table
        )
        .values(album_id=11, title="Wow", content="WOWOWOOWOW", created_at=datetime.datetime.now())
    )
    await database.execute(query)