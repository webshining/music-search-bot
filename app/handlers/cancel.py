from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from loader import _, dp


@dp.message_handler(Command('cancel'), state='*')
async def cancel_handler(message: Message, state: FSMContext):
    await state.finish()
    await message.answer(_('All state reset!'))