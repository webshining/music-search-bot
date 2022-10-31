from pydantic import BaseModel

from loader import db
from .song import Song


class User(BaseModel):
    id: int
    name: str
    username: str
    lang: str
    songs: list[Song] = []


users_collection = db["users"]
