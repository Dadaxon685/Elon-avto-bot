from aiogram import Dispatcher,Bot
from aiogram.types import Message
from data.config import token
import logging
import asyncio
from users.usermain import user_router
from users.admin import admin_router
# from group.main import group_router
logging.basicConfig(level=logging.INFO)
bot= Bot(token=token)
dp =Dispatcher()
# from users.admin import admin_router

# dp.include_router(echo.user_router)
# dp.include_router(group_router)
dp.include_router(admin_router)
dp.include_router(user_router)






async def main():
    await bot.send_message(chat_id= 5148276461 ,text ="bot ishga tushdi")
    await dp.start_polling(bot)
    
if __name__ =="__main__":
    try: 
        asyncio.run(main())
    except:
        print('tugadi')