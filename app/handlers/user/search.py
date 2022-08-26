from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from app.keyboards import get_musics_markup
from loader import dp
from utils import get_musics, get_text


class SearchState(StatesGroup):
    name = State()


@dp.message_handler(Command('search'))
async def search_handler(message: Message):
    await message.answer('Введите название песни:')
    await SearchState.name.set()


@dp.message_handler(content_types=['text'], state=SearchState.name)
async def search_name_handler(message: Message, state: FSMContext):
    musics = get_musics(message.text)
    if not musics:
        await message.answer('Песня не была найдена, введите другое название:')
    else:
        await message.answer('Выберете песню:', reply_markup=get_musics_markup('search', musics))
        await state.finish()


@dp.callback_query_handler(lambda call: call.data.startswith('search'))
async def search_music_handler(call: CallbackQuery):
    text = get_text(call.data[7:])
    await call.message.edit_text(text, reply_markup=None)
