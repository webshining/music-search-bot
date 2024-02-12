from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.utils.i18n import I18n
from redis.asyncio.client import Redis

from data.config import I18N_DOMAIN, I18N_PATH, TELEGRAM_BOT_TOKEN, RD_URI

bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode="HTML")
storage = RedisStorage(Redis.from_url(RD_URI))
dp = Dispatcher(storage=storage)

i18n = I18n(path=I18N_PATH, domain=I18N_DOMAIN)
_ = i18n.gettext
