from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from loader import _


def get_song_markup(data: str, id: int, chords: bool = True):
    markup = InlineKeyboardBuilder()

    buttons = [
        InlineKeyboardButton(text=_("Back"), callback_data=f'{data}_back'),
        InlineKeyboardButton(text=_("Chords: On") if not chords else _("Chords: Off"),
                             callback_data=f'{data}_chords_{chords}_{id}'),
        InlineKeyboardButton(text=_("Music"), callback_data=f'{data}_music_{id}', ),
    ]
    markup.add(*buttons)
    markup.adjust(2)

    return markup.as_markup()
