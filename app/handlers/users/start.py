from aiogram.filters import Command
from aiogram.types import Message

from app.commands import get_default_commands
from loader import dp


@dp.message(Command("start"))
async def _start(message: Message):
    text = '👋 Hello <b>{}</b>\n\nCommands:'.format(message.from_user.full_name)
    for command in get_default_commands(message.from_user.language_code):
        text += f'\n{command.command} - {command.description}'

    text += '\n\nAuthor: <b>@webshining</b>'
    await message.answer(text)
