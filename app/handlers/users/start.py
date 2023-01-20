from aiogram.types import Message
from aiogram.filters import Command


from loader import dp, _
from app.commands import get_default_commands


@dp.message(Command("start"))
async def _start(message: Message):
    text = _('👋 Hello <b>{}</b>\n\nCommands:').format(message.from_user.full_name)
    for command in get_default_commands(message.from_user.language_code):
        text += f'\n{command.command} - {command.description}'
    
    text += _('\n\nAuthor: <b>@webshining</b>')
    await message.answer(text)
