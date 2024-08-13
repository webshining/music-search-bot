from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from database.models import Song


class SongsCallback(CallbackData, prefix="songs"):
    data: str
    id: int


def get_songs_markup(data: str, songs: list[Song]):
    builder = InlineKeyboardBuilder()

    buttons = [
        InlineKeyboardButton(
            text=f"{i + 1}", callback_data=SongsCallback(data=data, id=s.id).pack()
        )
        for i, s in enumerate(songs)
    ]
    builder.add(*buttons)
    builder.adjust(2)

    return builder.as_markup()
