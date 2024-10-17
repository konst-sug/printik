import logging
import datetime
import aiogram.utils.markdown as md
from selenium import webdriver

from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from loader import dp, admin, bot
from utils.winderToTg import winderOrder_to_tg, winderConstr_to_tg
from config_data.config_one_test import url, test_data, chrome_options
from keyboards.winder_buttons import winder_markup
from lexicon.lexicon_ru import LEXICON_RU


logging.basicConfig(level=logging.INFO)


@dp.message_handler(lambda x: int(x.from_user.id) in admin, state="winder")
async def winder_menu(message: types.Message,state: FSMContext):
    await message.answer(f"Тесты Flagwinder, {LEXICON_RU['exit']}",reply_markup=winder_markup)
    await state.set_state("add_wind")
   

# ------------------------Flagwinder tests BLOCK  ----------------------------------
@dp.message_handler(state="add_wind", content_types=["text"])
async def create_test(message: types.Message, state: FSMContext):
    driver = webdriver.Chrome(options=chrome_options)
    status = message.text
    text = LEXICON_RU[status]
    if status == 'Форма заказа':
        await message.answer(text)
        res = winderOrder_to_tg(driver, url, test_data, False)
        await bot.send_photo(message.chat.id, open(f'{res[-1]}',"rb"),caption=res[:-1])
    elif status == 'Форма заказа + заказ':
        await message.answer(text)
        res = winderOrder_to_tg(driver, url, test_data, True)
        await bot.send_photo(message.chat.id, open(f'{res[-1]}',"rb"),caption=res[:-1])
    elif status == 'Флаг-расчет':
        await message.answer(text)
        res = winderConstr_to_tg(driver, url, test_data, False)
        await bot.send_photo(message.chat.id, open(f'{res[-1]}',"rb"),caption=res[:-1])
    elif status == 'Флаг-расчет + заказ':
        await message.answer(text)
        await bot.send_photo(message.chat.id, open(f'{res[-1]}',"rb"),caption=res[:-1])
    elif status == 'Флаг-расчет + почта':
        await message.answer(text)
        res = winderConstr_to_tg(driver, url, test_data, False)
        await message.answer(res)
    else: 
        text = LEXICON_RU['error']             
        print(text)
        await message.answer(text)
    logging.info(res)   

