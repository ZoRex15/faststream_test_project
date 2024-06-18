import asyncio

from aiogram import Dispatcher, Bot

from faststream import FastStream

from app.tg_bot.factory import create_dishka


async def main():
    dishka = create_dishka()
    dp = await dishka.get(Dispatcher)
    bot = await dishka.get(Bot)
    fast_stream_app = await dishka.get(FastStream)
    try:
        await fast_stream_app.start()
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await dishka.close()


if __name__ == '__main__':
    asyncio.run(main())
    




