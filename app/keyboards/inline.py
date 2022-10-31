from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from loader import _


def get_inline_markup():
    markup = InlineKeyboardBuilder()

    buttons = [
        InlineKeyboardButton(text=_("Search in another chat"), switch_inline_query="")
    ]
    markup.add(*buttons)

    return markup.as_markup()
