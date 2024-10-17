
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config_data.config_maker import load_config, load_data
from config_data.config_one_test import env_path

config_bot = load_config(env_path)
admin_data = load_data(env_path)

token = config_bot.tg_bot.token
bot = Bot(token)
dp = Dispatcher(bot,storage=MemoryStorage())

key1 = 1475104793

admin = admin_data.admin
query = dict()
admin_waybills_dict = dict()
#admin = [1622457532,1000341903,1475104793]  # 415820274, 667168664, 279262591


functions_in_acc = {
    
}
