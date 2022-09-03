from peewee import PrimaryKeyField, CharField, ForeignKeyField, TextField
from .base import BaseModel
from .user import User


class Music(BaseModel):
    id = PrimaryKeyField(primary_key=True)
    href = CharField(null=False)
    name = CharField(null=False)
    text = TextField(null=True)
    user = ForeignKeyField(User, backref='musics', null=False)

    class Meta:
        table_name = "musics"
