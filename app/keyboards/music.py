from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from loader import _


def get_music_markup(data: str):
    markup = InlineKeyboardBuilder()

    buttons = [
        InlineKeyboardButton(text=_("Music"), callback_data=f'music_{data}'),
        InlineKeyboardButton(text=_("Back"), callback_data=f'music_back'),
    ]
    markup.add(*buttons)
    markup.adjust(2)

    return markup.as_markup()
