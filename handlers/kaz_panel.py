import logging
import datetime
import aiogram.utils.markdown as md

from selenium import webdriver
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from loader import dp, admin, bot
from config_data.config_one_test import test_data, url, foto_url, chrome_options
from utils.kazToTg import kazOrder_to_tg, kazConstructor_to_tg
from keyboards.kaz_buttons import kaz_markup
from lexicon.lexicon_ru import LEXICON_RU

logging.basicConfig(level=logging.INFO)


@dp.message_handler(lambda x: int(x.from_user.id) in admin, state="kaz")
async def kaz_menu(message: types.Message,state: FSMContext):
    await message.answer(f"Тесты Print-Kaz, {LEXICON_RU['exit']}",reply_markup=kaz_markup)
    await state.set_state("add_kaz")
   

# ------------------------Kaz constructor tg BLOCK  ----------------------------------
@dp.message_handler(state="add_kaz", content_types=["text"])
async def kaz_test(message: types.Message, state: FSMContext):
    driver = webdriver.Chrome(options=chrome_options)
    now_datetime = datetime.datetime.now()
    data_task = await state.get_data()
    status = message.text
    text = LEXICON_RU[status]
    if status == 'Форма заказа':
        await message.answer(text)
        res = kazOrder_to_tg(driver, url, test_data, False)
        await bot.send_photo(message.chat.id, open(f'{res[-1]}',"rb"),caption=res[:-1])
    elif status == 'Форма заказа + заказ':
        await message.answer(text)
        res = kazOrder_to_tg(driver, url, test_data, True)
        await message.answer(res)
    elif status == 'Редактор':
        await message.answer(text)
        res = kazConstructor_to_tg(driver, url, test_data, False)
        await bot.send_photo(message.chat.id, open(f'{res[-1]}',"rb"),caption=res[:-1])
    elif status == 'Редактор + заказ':
        await message.answer(text)
        res = kazConstructor_to_tg(driver, url, test_data, True)
        await message.answer(res)
    else: 
        text = LEXICON_RU['error']             
        print(text)
        await message.answer(text)
    logging.info(res)
