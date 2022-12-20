from peewee import PrimaryKeyField, CharField

from .base import BaseModel


class User(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    username = CharField(null = True)
