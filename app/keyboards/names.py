from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from utils.api import Song


def get_songs_markup(data: str, songs: list[Song]):
    builder = InlineKeyboardBuilder()

    buttons = [
        InlineKeyboardButton(text=f"{i + 1}", callback_data=f'{data}_{s.id}') for i, s in enumerate(songs)
    ]
    builder.add(*buttons)
    builder.adjust(2)

    return builder.as_markup()
