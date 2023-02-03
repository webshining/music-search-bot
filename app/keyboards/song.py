from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from loader import _


def get_song_markup(chords: bool = False):
    markup = InlineKeyboardBuilder()

    buttons = [
        InlineKeyboardButton(text=_("Back"), callback_data=f'song_back'),
        InlineKeyboardButton(text=_("Chords") + (": On" if chords else ": Off"), callback_data=f'song_chords_{not chords}'),
    ]
    markup.add(*buttons)
    markup.adjust(2)

    return markup.as_markup()
