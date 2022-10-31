from aiogram.types import Message
from aiogram.filters import Command


from loader import dp, _
from app.keyboards import get_inline_markup


@dp.message(Command("start"))
async def _start(message: Message):
    await message.answer(_('👋 Hello <b>{}</b>\n🚫 The library is temporarily disabled').format(message.from_user.full_name), reply_markup=get_inline_markup())
