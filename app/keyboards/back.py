from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from loader import _


def get_back_markup(data: str):
    markup = InlineKeyboardBuilder()

    buttons = [
        InlineKeyboardButton(text=_("Back"), callback_data=f'{data}_back')
    ]
    markup.add(*buttons)

    return markup.as_markup()
