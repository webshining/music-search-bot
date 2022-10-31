from pydantic import BaseModel


class Song(BaseModel):
    href: str
    name: str
    text: str
