from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher.storage import FSMContext
from loader import dp


@dp.message_handler(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    await state.update_data(name = message.from_user.full_name)
    await message.answer(f'Hello <b>{message.from_user.full_name}</b>')