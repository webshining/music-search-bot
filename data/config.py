from environs import Env
from peewee import SqliteDatabase, PostgresqlDatabase

env = Env()
env.read_env()

TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN')
ADMINS = env.list('ADMINS', subcast=int, default=[])

DB_NAME = env.str('DB_NAME', None)
DB_USER = env.str('DB_USER', None)
DB_PASS = env.str('DB_PASS', None)
DB_HOST = env.str('DB_HOST', None)
DB_PORT = env.int('DB_PORT', None)

RD_DB = env.str('RD_DB', None)
RD_PASS = env.str('RD_PASS', None)
RD_HOST = env.str('RD_HOST', None)
RD_PORT = env.int('RD_PORT', None)

I18N_DOMAIN = 'bot'

if DB_PORT and DB_HOST and DB_PASS and DB_USER and DB_NAME:
    database = PostgresqlDatabase(DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
else:
    database = SqliteDatabase('./data/database.sqlite')
