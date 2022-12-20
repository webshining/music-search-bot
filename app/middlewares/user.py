from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Update
from database.services import get_or_create_user


class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        global from_user
        if event.message:
            from_user = event.message.from_user
        elif event.callback_query:
            from_user = event.callback_query.from_user
        elif event.inline_query:
            from_user = event.inline_query.from_user
        user = await get_or_create_user(from_user.id, name=from_user.full_name, username=from_user.username if from_user.username else None)
        data['user'] = user
        return await handler(event, data)