from aiogram import Bot, Dispatcher, types
from data.config import RD_DB, RD_HOST, RD_PORT, RD_PASS, TELEGRAM_BOT_TOKEN
from utils import logger
from app.middlewares import i18n
_ = i18n.gettext

bot = Bot(TELEGRAM_BOT_TOKEN, disable_web_page_preview=True, parse_mode=types.ParseMode.HTML)
if RD_DB and RD_HOST and RD_PORT:
    from aiogram.contrib.fsm_storage.redis import RedisStorage2

    storage = RedisStorage2(RD_HOST, RD_PORT, RD_DB, RD_PASS)
else:
    from aiogram.contrib.fsm_storage.memory import MemoryStorage

    storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def on_startup(dispatcher):
    from app.middlewares import setup_middlewares
    from app.commands import set_default_commands
    setup_middlewares(dp)
    await set_default_commands()
    logger.info('Bot started!')


async def on_shutdown(dispatcher):
    await bot.delete_my_commands()
    for lg in i18n.available_locales:
        await bot.delete_my_commands(language_code=lg)
    logger.warning('Bot shutting down!')
