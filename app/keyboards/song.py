from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def get_song_markup(data: str, chords: bool = False):
    markup = InlineKeyboardBuilder()

    buttons = [
        InlineKeyboardButton(text="Back", callback_data=f'{data}_back'),
        # InlineKeyboardButton(text="Chords" + (": On" if chords else ": Off"),
        #                      callback_data=f'{data}_chords_{not chords}'),
    ]
    markup.add(*buttons)
    markup.adjust(2)

    return markup.as_markup()
