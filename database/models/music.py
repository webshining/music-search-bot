from peewee import IntegerField, CharField, ForeignKeyField
from .base import BaseModel
from .user import User


class Music(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField(null=False)
    file_id = CharField(null=False)
    text = CharField(null=True)
    user = ForeignKeyField(User, backref='musics', null=False)

    class Meta:
        table_name = 'musics'
