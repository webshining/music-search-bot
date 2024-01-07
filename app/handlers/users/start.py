from aiogram.filters import Command
from aiogram.types import Message

from app.commands import get_default_commands
from loader import dp, _


@dp.message(Command("start"))
async def _start(message: Message):
    text = _('👋 Hello <b>{}</b>').format(message.from_user.full_name) + "\n\n" + _('Commands:')
    for command in get_default_commands(message.from_user.language_code):
        text += f'\n{command.command} - {command.description}'

    text += "\n\n" + _(
        'If you see an error in the text display or anything else, please let me know: <b>@webshining</b>')
    await message.answer(text)
