from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart
from loader import dp


@dp.message_handler(CommandStart())
async def start_handler(message: Message):
    await message.answer(f'Hello <b>{message.from_user.full_name}</b>')
