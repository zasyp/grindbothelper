import asyncio
from aiogram import Bot, Dispatcher, F
from app.main.stuff.handlers import router


async def main():
    bot = Bot(token="6547786362:AAGkPf5yL_cUcQK0MIDxNy46PJiLINsiBUo")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
