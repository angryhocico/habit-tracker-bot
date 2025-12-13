import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import router
from database import init_db

async def main():
    load_dotenv()
    init_db()
    print("База данных инициализирована.")
    
    token = os.getenv("BOT_TOKEN")
    
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=token)
    dp = Dispatcher()
    
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")