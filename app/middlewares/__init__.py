from aiogram import Dispatcher

from .inter import i18n_middleware


def setup_middlewares(dp: Dispatcher):
    dp.update.middleware(i18n_middleware)
