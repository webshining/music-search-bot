import asyncio
import sys

from app.handlers import dp
from loader import bot


async def on_startup():
    from app.commands import set_default_commands
    from app.middlewares import setup_middlewares
    await set_default_commands()
    setup_middlewares(dp)
    print("Bot started!")


async def on_shutdown():
    print("Bot stoped!")


def main() -> None:
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.run_polling(bot)


if __name__ == "main":
    async def on_startup():
        from app.commands import set_default_commands
        from app.middlewares import setup_middlewares
        await set_default_commands()
        setup_middlewares(dp)
        print("Bot started!")
        await bot.session.close()
        sys.exit(0)


    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.run_polling(bot)

if __name__ == "__main__":
    main()
