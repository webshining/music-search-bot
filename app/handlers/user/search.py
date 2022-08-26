from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from app.keyboards import get_musics_markup, get_music_markup
from loader import dp, _
from utils import get_musics, get_text


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
        await state.update_data(musics = musics)


@dp.callback_query_handler(lambda call: call.data.startswith('search'))
async def search_text_handler(call: CallbackQuery, state: FSMContext, user):
    if call.data[7:] == 'back':
        data = await state.get_data()
        await call.message.edit_text(_('Select song:'), reply_markup=get_musics_markup('search', data.get('musics')))
    else:
        text = get_text(call.data[7:])
        await call.message.edit_text(text, reply_markup=get_music_markup('search', False))
