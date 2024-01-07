from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.utils.i18n import I18n
from redis.asyncio.client import Redis

from data.config import (I18N_DOMAIN, I18N_PATH, RD_DB, RD_HOST, RD_PASS,
                         RD_PORT, TELEGRAM_BOT_TOKEN, RD_USER, RD_URL)

bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode="HTML")
if RD_URL:
    storage = RedisStorage(Redis.from_url(RD_URL))
elif RD_DB and RD_HOST and RD_PORT:
    storage = RedisStorage(Redis(db=RD_DB, host=RD_HOST, port=RD_PORT, password=RD_PASS, username=RD_USER))
else:
    storage = MemoryStorage()
dp = Dispatcher(storage=storage)

i18n = I18n(path=I18N_PATH, domain=I18N_DOMAIN)
_ = i18n.gettext
