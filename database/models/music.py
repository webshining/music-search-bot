from peewee import PrimaryKeyField, CharField, ForeignKeyField, TextField
from .base import BaseModel
from .user import User


class Music(BaseModel):
    id = PrimaryKeyField()
    href = CharField(null=False)
    name = CharField(null=False)
    text = TextField(null=False)
    user = ForeignKeyField(User, backref='musics', null=False)

    class Meta:
        table_name = 'musics'
