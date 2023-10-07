from pathlib import Path

from environs import Env

env = Env()
env.read_env()


DIR = Path(__file__).absolute().parent.parent

TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN', None)

ADMINS = env.list('ADMINS', subcast=int, default=[])

RD_DB = env.int('RD_DB', None)
RD_HOST = env.str('RD_HOST', None)
RD_PORT = env.int('RD_PORT', None)
RD_PASS = env.str('RD_PASS', None)

SELENIUM_REMOTE = env.str('SELENIUM_REMOTE', None)

I18N_PATH = f'{DIR}/data/locales'
I18N_DOMAIN = 'bot'