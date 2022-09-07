from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from loader import dp, _
from app.keyboards import get_musics_markup, get_music_markup
from database import get_music, delete_music, create_music
from utils import get_music_data


@dp.message_handler(Command('library'))
async def library_handler(message: Message, user):
    musics = user.musics
    if not musics:
        return await message.answer(_("Library is empty"))
    await message.answer(_('Select song:'), reply_markup=get_musics_markup('library', musics))


@dp.callback_query_handler(lambda call: call.data.startswith('library'))
async def library_callback_handler(call: CallbackQuery, user):
    call_data = call.data.split('_')
    musics = user.musics
    if call_data[1] == 'back':
        await call.message.edit_text(text=_('Select song:') if musics else _('Library is empty'), reply_markup=get_musics_markup('library', musics) if musics else None)
    elif call_data[1] == 'delete':
        delete_music(call_data[2], user.id)
        await call.message.edit_reply_markup(reply_markup=get_music_markup('library', False, call_data[2]))
    elif call_data[1] == 'add':
        music_href, name, text = get_music_data(call_data[2])
        create_music(call_data[2], music_href, name, text, user.id)
        await call.message.edit_reply_markup(reply_markup=get_music_markup('library', True, call_data[2]))
    elif call_data[1] == 'music':
        music = get_music(href=call_data[2])
        await call.message.answer_audio(audio=f'https://holychords.pro/uploads/music{music.music_href}')
    else:
        music = get_music(href=call_data[1])
        await call.message.edit_text(music.text, reply_markup=get_music_markup('library', True, call_data[1]))
    await call.answer()
