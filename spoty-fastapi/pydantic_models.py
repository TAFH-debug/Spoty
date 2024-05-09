from pydantic import BaseModel

class AlbumId(BaseModel):
    album_id: int

class Review(BaseModel):
    album_id: int
    score: int
    content: str
    username: str
    password: str
    
class User(BaseModel):
    username: str
    password: str