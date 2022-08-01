from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat
from loader import _, i18n, bot
from .default import get_default_commands


def get_admin_commands(language_code: str = 'en'):
    commands = get_default_commands(language_code).extend([
        BotCommand('/message', _('send message', locale=language_code)),
        BotCommand('/users', _('get all users', locale=language_code))
    ])
    return commands


async def set_admin_commands(user_id: int, language_code: str):
    await bot.set_my_commands(get_admin_commands(language_code), scope=BotCommandScopeChat(user_id))
