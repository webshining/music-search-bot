from xmlrpc.client import boolean
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import _


def get_music_markup(data: str, delete: boolean):
    markup = InlineKeyboardMarkup(row_width=2)
    
    buttons = [
        # InlineKeyboardButton(text=_('Remove from library') if delete else _('Add to library'), 
        #                      callback_data=f'{data}_{"delete" if delete else "add"}'),
        InlineKeyboardButton(text=_('Back'), callback_data=f'{data}_back')
    ]
    markup.add(*buttons)
    
    return markup