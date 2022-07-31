from aiogram.types import Message
from aiogram.dispatcher.middlewares import BaseMiddleware


class UserMiddleware(BaseMiddleware):
    @staticmethod
    async def on_process_message(message: Message, data: dict):
        pass