from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def get_songs_markup(data: str, songs: list):
    builder = InlineKeyboardBuilder()

    buttons = [
        InlineKeyboardButton(text=f"{song['name']} - {song['artist']}", callback_data=f'{data}_{song["href"]}') for song in songs
    ]
    builder.add(*buttons)
    builder.adjust(2)

    return builder.as_markup()
