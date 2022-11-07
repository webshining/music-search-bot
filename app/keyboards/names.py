from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def get_names_markup(data: str, names: list):
    builder = InlineKeyboardBuilder()

    buttons = [
        InlineKeyboardButton(text=name['name'], callback_data=f'{data}_{name["href"]}') for name in names
    ]
    builder.add(*buttons)
    builder.adjust(2)

    return builder.as_markup()
