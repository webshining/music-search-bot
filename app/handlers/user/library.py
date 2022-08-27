from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from loader import dp, _
from app.keyboards import get_musics_markup
from database import get_music


@dp.message_handler(Command('library'))
async def linrary_handler(message: Message, user):
    musics = user.musics
    if not musics:
        return await message.answer(_("Library is empty!"))
    await message.answer(_('Select song:'), reply_markup=get_musics_markup('library', musics))


@dp.callback_query_handler(lambda call: call.data.startswith('library'))
async def library_callback_handler(call: CallbackQuery):
    music = get_music(href=call.data[8:])
    await call.message.edit_text(music.text)