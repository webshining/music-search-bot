from .i18n import i18n
from .user import UserMiddleware


def setup_middlewares(dp):
    dp.middleware.setup(i18n)
    dp.middleware.setup(UserMiddleware())
