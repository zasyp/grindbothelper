import asyncio
from aiogram import Bot, Dispatcher
from app.main.stuff.handlers import router
from app.main.database.db import init_db

API_TOKEN = "6547786362:AAGkPf5yL_cUcQK0MIDxNy46PJiLINsiBUo"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

dp.include_router(router)

async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")