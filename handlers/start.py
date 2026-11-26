from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def get_start(message: Message):
    await message.answer("hello!")
    
@router.message(F.text.contains("хряк"))
async def com(message: Message):
    await message.answer("lol")