import asyncio
from create_bot import bot, dp
from handlers.start import router

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
