from aiogram import executor, types
from app.middlewares.inter import i18n
from loader import dp, bot
from data.config import ADMINS
from utils import logger


async def on_startup(dispatcher):
    from app.commands import set_default_commands
    for admin_id in ADMINS:
        try:
            await bot.send_message(chat_id=admin_id, text='Bot started!')
        except:
            pass
    await set_default_commands()
    logger.info('Bot started!')


async def on_shutdown(dispatcher):
    await bot.delete_my_commands(scope=types.BotCommandScopeDefault())
    for lang in i18n.available_locales:
        await bot.delete_my_commands(scope=types.BotCommandScopeDefault(), language_code=lang)
    for admin_id in ADMINS:
        try:
            await bot.send_document(admin_id, types.InputFile('./data/database.sqlite'))
            await bot.send_message(chat_id=admin_id, text='Bot shutting down!')
        except:
            pass
    logger.info('Bot shutting down!')


if __name__ == '__main__':
    from app.middlewares import setup_middlewares
    import app.filters, app.handlers
    setup_middlewares(dp)
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
