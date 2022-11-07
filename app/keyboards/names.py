from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def get_names_markup(data: str, names: list):
    markup = InlineKeyboardBuilder()

    buttons = [
        InlineKeyboardButton(text=name['name'], callback_data=f'{data}_{name["href"]}') for name in names
    ]
    markup.adjust(2)
    markup.add(*buttons)

    return markup.as_markup()
