from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select, desc, insert
import datetime
from os import environ
from models.reviews import reviews_table
from models.users import users_table
from models.albums import albums_table
import databases
from pydantic_models import *
import json 

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

async def check_credentials(data: User):
    query1 = (
        select(
            users_table.c.id,
            users_table.c.name,
            users_table.c.password
        )
        .where(users_table.c.name == data.username)
    )
    user = await database.fetch_all(query1)
    if len(user) == 0 or user[0].password != data.password:
        return None
    return user[0]

async def get_user(username: str):
    query1 = (
        select(
            users_table.c.id,
            users_table.c.name,
            users_table.c.password
        )
        .where(users_table.c.name == username)
    )
    user = await database.fetch_all(query1)
    if len(user) == 0:
        return None
    return user[0]

@app.on_event("startup")
async def startup():
    await database.connect()
    with open("./example_data.json", "r") as file:
        obj: dict = json.load(file)
        if ('loaded' in obj.keys()):
            return
        
    query1 = insert(reviews_table)
    query2 = insert(albums_table)
    
    for i in obj['reviews']:
        query1 = query1.values(
            id=i['id'],
            album_id=i['album_id'],
            username=i['username'],
            created_at=datetime.datetime.now(),
            content=i['content'],
            user_id=i['user_id'],
            score=i['score']
        )
        
    for i in obj['albums']:
        query3 = query2.values(
            id=i['id'],
            title=i['title'],
            author=i['author'],
            genre=i['genre'],
            description=i['description'],
            image=i['image']
        )
        await database.execute(query3)
    
    with open("./example_data.json", "w+") as file:
        obj['loaded'] = True
        json.dump(obj, file)
    
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    
@app.get("/api/trends")
async def trends():
    
    query = (
        select(
            albums_table.c.id,
            albums_table.c.title,
            albums_table.c.author,
            albums_table.c.genre,
            albums_table.c.description,
            albums_table.c.image
        )
    )
    albums = await database.fetch_all(query)
    body = {
        "trends": albums[:(len(albums) // 2)],
        "albums": albums
    }
    return body

@app.get("/api/get_all_reviews")
async def get__all_reviews():
    query = (
        select(
            reviews_table.c.id,
            reviews_table.c.album_id,
            reviews_table.c.username,
            reviews_table.c.created_at,
            reviews_table.c.content,
            reviews_table.c.user_id,
            reviews_table.c.score
        )
        .order_by(reviews_table.c.created_at)
    )
    return await database.fetch_all(query)

@app.get("/api/get_all_users")
async def get__all_users():
    query = (
        select(
            users_table.c.id,
            users_table.c.name,
            users_table.c.password
        )
    )
    return await database.fetch_all(query)

@app.post("/api/get_reviews")
async def get_reviews(body: AlbumId):
    query = (
        select(
            reviews_table.c.id,
            reviews_table.c.album_id,
            reviews_table.c.username,
            reviews_table.c.created_at,
            reviews_table.c.score,
            reviews_table.c.content,
            reviews_table.c.user_id
        )
        .where(reviews_table.c.album_id == body.album_id)
        .order_by(desc(reviews_table.c.created_at))
    )
    
    query2 = select(
        albums_table.c.id,
        albums_table.c.title,
        albums_table.c.author,
        albums_table.c.genre,
        albums_table.c.description,
        albums_table.c.image
    ).where(albums_table.c.id == body.album_id)
    
    reviews = await database.fetch_all(query)
    album = await database.fetch_all(query2)
    if len(album) == 0:
        return {"error": "Such album doesn't exist."}
    return { "reviews": reviews, "album": album[0] }

@app.post("/api/create_review")
async def create_review(data: Review):
    user = await check_credentials(data)
    print("W")
    if not user:
        return {"error": "Invalid credentials"}
    query = (
        insert(
            reviews_table
        )
        .values(album_id=data.album_id, username=data.username,
                content=data.content, created_at=datetime.datetime.now(),
                user_id=user.id, score=data.score)
    )
    print("W")
    await database.execute(query)

@app.post("/api/register")
async def register(data: User):
    query = (
        insert(
            users_table
        )
        .values(name=data.username, password=data.password)
    )
    user = await get_user(data.username)
    if user:
        return {"error": "User exists"}
    await database.execute(query)
    
    