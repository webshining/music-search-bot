def setup_middlewares(dp):
    from .user import UserMiddleware
    from .inter import i18n
    from .logging import LoggingMiddleware
    dp.setup_middleware(UserMiddleware())
    dp.setup_middleware(i18n)
    dp.setup_middleware(LoggingMiddleware())
