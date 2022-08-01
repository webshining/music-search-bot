from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat
from loader import _, i18n, bot


def get_default_commands(language_code: str = 'en'):
    commands = [
        BotCommand('/start', _('start chat', locale=language_code)),
        BotCommand('/help', _('help to use', locale=language_code)),
        BotCommand('/search', _('search music', locale=language_code)),
        BotCommand('/library', _('library', locale=language_code)),
        BotCommand('/add', _('add to library', locale=language_code))
    ]
    return commands


async def set_default_commands():
    await bot.set_my_commands(get_default_commands(), scope=BotCommandScopeDefault())
    for language_code in i18n.available_locales:
        await bot.set_my_commands(get_default_commands(language_code), scope=BotCommandScopeDefault(), language_code=language_code)


async def set_user_commands(user_id: int, language_code: str):
    await bot.set_my_commands(get_default_commands(language_code), scope=BotCommandScopeChat(user_id))
