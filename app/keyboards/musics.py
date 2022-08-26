from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_musics_markup(data: str, musics: list):
    markup = InlineKeyboardMarkup(row_width=2)

    buttons = [
        InlineKeyboardButton(text=music['name'] or music.name, callback_data=f'{data}_{music["href"] or music.id}') for
        music in musics
    ]
    markup.add(*buttons)

    return markup
