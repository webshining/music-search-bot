from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat
from loader import _, i18n, bot


def get_default_commands(lang: str = 'en'):
    commands = [
        BotCommand('/start', _('start chat', locale=lang)),
        BotCommand('/help', _('help to use', locale=lang)),
        BotCommand('/search', _('search music', locale=lang)),
        BotCommand('/library', _('library', locale=lang)),
        BotCommand('/add', _('add to library', locale=lang)),
        BotCommand('/lang', _('change language', locale=lang))
    ]
    return commands


async def set_default_commands():
    await bot.set_my_commands(get_default_commands(), scope=BotCommandScopeDefault())
    for lang in i18n.available_locales:
        await bot.set_my_commands(get_default_commands(lang), scope=BotCommandScopeDefault(), language_code=lang)


async def set_user_commands(user_id: int, language_code: str):
    await bot.set_my_commands(get_default_commands(language_code), scope=BotCommandScopeChat(user_id))
