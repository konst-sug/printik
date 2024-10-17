import logging
import logging.config 
import threading
import handlers

from aiogram import executor
from loader import dp
from everlasting_thread import sessions_manager

from logging_settings import logging_config


logging.basicConfig(level=logging.INFO)
 
logging.config.dictConfig(logging_config)




async def start_bot(dp):
    task = threading.Thread(target=sessions_manager)
    task.start()


executor.start_polling(dp,skip_updates=True,on_startup=start_bot)

