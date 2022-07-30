from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import RD_DB, RD_HOST, RD_PORT, RD_PASS, TELEGRAM_BOT_TOKEN

bot = Bot(TELEGRAM_BOT_TOKEN, disable_web_page_preview=True, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
if RD_DB and RD_HOST and RD_PORT:
    storage = RedisStorage2(RD_HOST, RD_PORT, RD_DB, RD_PASS)
dp = Dispatcher(bot, storage=storage)