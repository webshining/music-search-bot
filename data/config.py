from pathlib import Path

from environs import Env

env = Env()
env.read_env()

DIR = Path(__file__).absolute().parent.parent

TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN', None)

ADMINS = env.list('ADMINS', subcast=int, default=[])

RD_DB = env.int('RD_DB', 5)
RD_HOST = env.str('RD_HOST', "localhost")
RD_PORT = env.int('RD_PORT', 6379)

RD_URI = env.str('RD_URI', default=f"redis://{RD_HOST}:{RD_PORT}/{RD_DB}")

I18N_PATH = f'{DIR}/data/locales'
I18N_DOMAIN = env.str('I18N_DOMAIN', 'bot')
