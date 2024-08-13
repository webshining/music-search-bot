from pydantic import Field, BaseModel

from .base import Base


class Song(BaseModel):
    id: int
    name: str
    artist: str


class User(Base):
    id: int
    songs: list[Song] = Field(default=[])


User.set_collection("user")
