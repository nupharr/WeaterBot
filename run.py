import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from src.handlers import router
from src.database import create_db

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_routers(router)


async def main() -> None:
    bot = Bot(token=TOKEN)

    await dp.start_polling(bot)


if __name__ == "__main__":
    create_db()
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
