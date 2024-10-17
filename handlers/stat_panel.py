import logging
import datetime
import aiogram.utils.markdown as md
from selenium import webdriver

from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from loader import dp, admin, bot
from utils.get_dash import dashboard_shot
from config_data.config_one_test import url, test_data, chrome_options
from keyboards.winder_buttons import winder_markup
from lexicon.lexicon_ru import LEXICON_RU


logging.basicConfig(level=logging.INFO)


@dp.message_handler(lambda x: int(x.from_user.id) in admin, state="local")
async def stat_menu(message: types.Message,state: FSMContext):
    await message.answer(f"Результаты , {LEXICON_RU['exit']}",reply_markup=types.ReplyKeyboardRemove())
    await state.set_state("dashboard")
    logging.info(state)
    driver = webdriver.Chrome()
    res = dashboard_shot(driver)
    await bot.send_photo(message.chat.id, open(f'{res[-1]}',"rb"),caption=res[:-1])  
    await state.set_state("dashboard")
   

# ------------------------Flagwinder tests BLOCK  ----------------------------------
@dp.message_handler(state="dashboard", content_types=["text"])
async def view_Tgtest(message: types.Message, state: FSMContext):
    logging.info(text)
    driver = webdriver.Chrome(options=chrome_options)
    now_datetime = datetime.datetime.now()
    data_task = await state.get_data()
    status = message.text
    text = LEXICON_RU[status]
    logging.info(status)
    if status == 'Statistics':
        await message.answer(text)
        res = dashboard_shot(driver)
        await bot.send_photo(message.chat.id, open(f'{res[-1]}',"rb"),caption=res[:-1])   
    else: 
        text = LEXICON_RU['error']             
        print(text)
        await message.answer(text)
    logging.info(res)
