from peewee import PrimaryKeyField, CharField

from .base import BaseModel


class Song(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    author = CharField()
    href = CharField()
