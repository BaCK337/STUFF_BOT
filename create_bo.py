from aiogram import Bot, Router, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from dotenv import load_dotenv

import asyncio
import os

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

async def main():
    await dp.start_polling()
    
if __name__ == "__main__":
    asyncio.run(main())