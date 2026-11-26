from aiogram import Bot, Router, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

