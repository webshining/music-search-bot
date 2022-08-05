from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from loader import dp, _
from utils import find_songs


class Search(StatesGroup):
    name = State()


@dp.message_handler(Command('search'))
async def search_handler(message: Message, state: FSMContext):
    message = await message.answer(_('Write the name of the song:'))
    await state.update_data(message_id=message.message_id)
    await Search.name.set()


@dp.message_handler(content_types=['text'], state=Search.name)
async def search_names_handler(message: Message, state: FSMContext):
    names = find_songs(message.text)
    await state.finish()

