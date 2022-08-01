from peewee import Model
from data.config import database


class BaseModel(Model):
    class Meta:
        database = database
