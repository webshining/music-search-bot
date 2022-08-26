from peewee import IntegerField, CharField, ForeignKeyField
from .base import BaseModel


class User(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    username = CharField(null=True)
    status = CharField(default='user')

    class Meta:
        table_name = 'users'
