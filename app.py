from decouple import config
from aiogram import Bot, Dispatcher
import asyncio, logging
from hendler.start import router


bot = Bot(token=config('TOKEN'))
dp = Dispatcher()



async def main():
    dp.include_router(router)
    
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')