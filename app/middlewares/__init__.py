from aiogram import Dispatcher

from .user import UserMiddleware


def setup_middlewares(dp: Dispatcher):
    dp.setup_middleware(UserMiddleware())
