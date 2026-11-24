from pathlib import Path
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile

import os
from dotenv import load_dotenv
import asyncio

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

@dp.message(F.text.lower().contains("охотник"))
async def hunter(message: Message):
    await message.reply("Ебать ты дурик!")
    await bot.send_message(text="wadsdaw")
        


async def main():
    await dp.start_polling(bot)
    
    
if __name__ == "__main__":
    asyncio.run(main())
