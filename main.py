from aiogram import executor
from loader import on_startup, on_shutdown


if __name__ == '__main__':
    import app.handlers
    executor.start_polling(app.handlers.dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
    