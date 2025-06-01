import asyncio

from aiogram import Dispatcher

from aiogram.methods import DeleteWebhook

from bot.routers import include_routers

from bot.bot import bot_mebel


dp = Dispatcher()


async def main():
   
    await bot_mebel(
        DeleteWebhook(drop_pending_updates=True)
        )
    
    await include_routers(dp=dp)

    await dp.start_polling(bot_mebel)


if __name__ == "__main__":
    try:
        print ("Бот запущен")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")