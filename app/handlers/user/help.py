from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from loader import dp, _


@dp.message_handler(Command('help'))
async def help_handler(message: Message):
    text = _('Hello <b>{}</b>\n'
             "I'm a holychords music search bot\n"
             "To control the bot you can use commands and buttons\n"
             "\nCommand list:\n"
             "<b>/start</b> - Start chat\n"
             "<b>/help</b> - Help to use\n"
             "<b>/search</b> - Search music\n"
             "<b>/library</b> - Library\n"
             "<b>/add</b> - Add music to library\n"
             "<b>/lang</b> - Change bot language\n"
             "\nCreator <b>@webshining</b>", locale=message.from_user.language_code)
    await message.answer(text.format(message.from_user.full_name))