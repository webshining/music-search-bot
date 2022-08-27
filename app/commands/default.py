from aiogram.types import BotCommandScopeDefault, BotCommand
from loader import bot, i18n, _


def get_default_commands(lang: str = 'en'):
    commands = [
        BotCommand('/start', _('start bot', locale=lang)),
        BotCommand('/search', _('search song', locale=lang)),
        BotCommand('/library', _('library', locale=lang)),
        BotCommand('/cancel', _('cancel', locale=lang))
    ]
    return commands


async def set_default_commands():
    await bot.set_my_commands(get_default_commands(), scope=BotCommandScopeDefault())
    for lang in i18n.available_locales:
        await bot.set_my_commands(get_default_commands(lang), scope=BotCommandScopeDefault(), language_code=lang)
