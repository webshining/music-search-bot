from aiogram import executor
from loader import dp


async def on_startup(dispatcher):
    from app.middlewares import setup_middlewares
    from app.commands import set_default_commands
    setup_middlewares(dp)
    await set_default_commands()


if __name__ == '__main__':
    import app.handlers
    executor.start_polling(dp, on_startup=on_startup)
