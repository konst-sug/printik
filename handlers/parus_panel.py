import logging
import time
import datetime
import aiogram.utils.markdown as md

from selenium import webdriver
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from loader import dp, admin, bot
from utils.parusToTg import *
from config_data.config_one_test import url, test_data, chrome_options
from keyboards.parus_buttons import parus_markup
from lexicon.lexicon_ru import LEXICON_RU


logging.basicConfig(level=logging.INFO)


@dp.message_handler(lambda x: int(x.from_user.id) in admin, state="parus")
async def parus_menu(message: types.Message,state: FSMContext):
    await message.answer(f"Тесты Flag-Parus, {LEXICON_RU['exit']}",reply_markup=parus_markup)
    time.sleep(1)
    await state.set_state("add_parus")
   

# ------------------------FlagParus tests BLOCK  --------------------

@dp.message_handler(state="add_parus", content_types=["text"])
async def create_test(message: types.Message, state: FSMContext):
    driver = webdriver.Chrome(options=chrome_options)
    now_datetime = datetime.datetime.now()
    data_task = await state.get_data()
    status = message.text
    text = LEXICON_RU[status]
    if status == 'Форма заказа':
        await message.answer(text)
        res = parusOrder_to_tg(driver, url, test_data, False)
        await message.answer(res)
    elif status == 'Форма заказа + заказ':
        await message.answer(text)
        res = parusOrder_to_tg(driver, url, test_data, True)
        await message.answer(res)
    elif status == 'Флаг-расчет':
        await message.answer(text)
        res = parusFlag_to_tg(driver, url, test_data, False)
        await bot.send_photo(message.chat.id, open(f'{res[-1]}',"rb"),caption=res[:-1])
    elif status == 'Флаг-расчет + заказ':
        await message.answer(text)
        res = parusFlag_to_tg(driver, url, test_data, True)
        await bot.send_photo(message.chat.id, open(f'{res[-1]}',"rb"),caption=res[:-1])
    elif status == 'Флаг-продукция':
        await message.answer(text)
        res = parusProds_to_tg(driver, url, test_data, False)
        await message.answer(res) 
    elif status == 'Флаг-продукция + заказ':
        await message.answer(text)
        res = parusProds_to_tg(driver, url, test_data, True)
        await message.answer(res)
    elif status == 'Редактор Cosuv':
        await message.answer(text)
        res = parusCosuv_to_tg(driver, url, test_data, False)
        await bot.send_photo(message.chat.id, open(f'{res[-1]}',"rb"),caption=res[:-1])
    elif status == 'Редактор Cosuv + заказ':
        await message.answer(text)
        res = parusCosuv_to_tg(driver, url, test_data, True)
        await bot.send_photo(message.chat.id, open(f'{res[-1]}',"rb"),caption=res[:-1])
    else: 
        text = LEXICON_RU['error']             
        print(text)
        await message.answer(text)
    logging.info(res)
    

