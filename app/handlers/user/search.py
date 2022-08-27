from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from app.keyboards import get_musics_markup, get_music_markup
from loader import dp, _
from utils import get_musics, get_text
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
    if call.data[7:].startswith('back'):
        data = await state.get_data()
        try:
            return await call.message.edit_text(_('Select song:'),
                                                reply_markup=get_musics_markup('search', get_musics(data.get('name'))))
        except:
            return await call.message.edit_text(_('Looks like the last search has been deleted.'), reply_markup=None)
    if call.data[7:].startswith('add'):
        href, name, text = get_text(call.data[11:])
        create_music(href, name, text, user)
        await call.message.edit_reply_markup(reply_markup=get_music_markup('search', True, href))
        return await call.message.answer(_('The song has been added to your library'))
    if call.data[7:].startswith('delete'):
        href, name, text = get_text(call.data[14:])
        try:
            delete_music(href, user)
        except:
            pass
        await call.message.edit_reply_markup(reply_markup=get_music_markup('search', False, href))
        return await call.message.answer(_('The song has been deleted from your library'))
    else:
        href, name, text = get_text(call.data[7:])
        await call.message.edit_text(text,
                                     reply_markup=get_music_markup('search', href in [m.href for m in user.musics],
                                                                   href))
