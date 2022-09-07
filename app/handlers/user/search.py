from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from app.keyboards import get_musics_markup, get_music_markup
from loader import dp, _
from utils import get_musics, get_music_data, get_music_href
from database import create_music, delete_music


class SearchState(StatesGroup):
    name = State()


@dp.message_handler(Command('search'))
async def search_handler(message: Message):
    await message.answer(_('Enter song title:'))
    await SearchState.name.set()


@dp.message_handler(content_types=['text'], state=SearchState.name)
async def search_name_handler(message: Message, state: FSMContext):
    musics = get_musics(message.text)
    if not musics:
        await message.answer(_('Song not found, please enter another title:'))
    else:
        await message.answer(_('Select song:'), reply_markup=get_musics_markup('search', musics))
        await state.finish()
        await state.update_data(name=message.text)


@dp.callback_query_handler(lambda call: call.data.startswith('search'))
async def search_text_handler(call: CallbackQuery, state: FSMContext, user):
    data = await state.get_data()
    call_data = call.data.split('_')
    if call_data[1] == 'back':
        if not data.get('name'):
            return await call.message.edit_text(text=_('Looks like the last search has been deleted') + '🤔', reply_markup=None)
        musics = get_musics(data.get('name'))
        await call.message.edit_text(text=_('Select song:'), reply_markup=get_musics_markup('search', musics))
    elif call_data[1] == 'delete':
        try:
            delete_music(call_data[2], user.id)
        except:
            pass
        await call.message.edit_reply_markup(reply_markup=get_music_markup('search', False, call_data[2]))
    elif call_data[1] == 'add':
        music_href, name, text = get_music_data(call_data[2])
        create_music(call_data[2], music_href, name, text, user.id)
        await call.message.edit_reply_markup(reply_markup=get_music_markup('search', True, call_data[2]))
    elif call_data[1] == 'music':
        music_href = get_music_href(href=call_data[2])
        await call.message.answer_audio(audio=f'https://holychords.pro/uploads/music{music_href}')
    else:
        music_href, name, text = get_music_data(call_data[1])
        if not text:
            return await call.message.edit_text(_('This song has no text') + '😥', reply_markup=None)
        await call.message.edit_text(text, reply_markup=get_music_markup('search', music_href in [u.music_href for u in user.musics], call_data[1]))
    await call.answer()
