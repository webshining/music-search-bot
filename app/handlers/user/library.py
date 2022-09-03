from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from loader import dp, _
from app.keyboards import get_musics_markup, get_music_markup
from database import get_music, delete_music, create_music
from utils import get_text


@dp.message_handler(Command('library'))
async def library_handler(message: Message, user):
    musics = user.musics
    if not musics:
        return await message.answer(_("Library is empty!"))
    await message.answer(_('Select song:'), reply_markup=get_musics_markup('library', musics))


@dp.callback_query_handler(lambda call: call.data.startswith('library'))
async def library_callback_handler(call: CallbackQuery, user):
    if call.data[8:].startswith('delete'):
        delete_music(call.data[15:], user.id)
        return await call.message.edit_reply_markup(reply_markup=get_music_markup('library', False, call.data[15:]))
    if call.data[8:].startswith('add'):
        href, name, text = get_text(call.data[12:])
        create_music(href, name, text, user)
        return await call.message.edit_reply_markup(reply_markup=get_music_markup('library', True, call.data[12:]))
    if call.data[8:].startswith('back'):
        return await call.message.edit_text(text=_('Select song:'), reply_markup=get_musics_markup('library', user.musics))
    music = get_music(href=call.data[8:])
    await call.message.edit_text(music.text, reply_markup=get_music_markup('library', True, call.data[8:]))
