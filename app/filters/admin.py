from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from database import get_user


class Admin(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin: bool):
        self.is_admin = is_admin

    async def check(self, message: Message):
        user = get_user(message.from_user.id)

        return user.status == 'admin'
