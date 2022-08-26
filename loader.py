from aiogram import Bot, Dispatcher, types
from peewee import PostgresqlDatabase, SqliteDatabase
from data.config import RD_DB, RD_HOST, RD_PORT, RD_PASS, DB_HOST, DB_PORT, DB_PASS, DB_NAME, DB_USER, TELEGRAM_BOT_TOKEN
from app.middlewares.inter import i18n


bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)
if RD_DB and RD_HOST and RD_PORT:
    from aiogram.contrib.fsm_storage.redis import RedisStorage2
    storage = RedisStorage2(RD_HOST, RD_PORT, RD_DB, RD_PASS)
else:
    from aiogram.contrib.fsm_storage.memory import MemoryStorage
    storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

if DB_PORT and DB_HOST and DB_PASS and DB_USER and DB_NAME:
    database = PostgresqlDatabase(DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
else:
    database = SqliteDatabase('./data/database.sqlite')


_ = i18n.gettext
