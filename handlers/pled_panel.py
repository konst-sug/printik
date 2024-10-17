import logging
import time
import datetime
import aiogram.utils.markdown as md

from selenium import webdriver
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.storage import FSMContext
from aiogram import types
from loader import dp, admin, bot
from keyboards.fotopled_buttons import pled_markup
from lexicon.lexicon_ru import LEXICON_RU
from utils.pledToTg import pledrOrder_to_tg, pledConstr_to_tg, pledCosuv_to_tg
from config_data.config_one_test import url, test_data, foto_url, chrome_options

logging.basicConfig(level=logging.INFO)


@dp.message_handler(lambda x: int(x.from_user.id) in admin, state="pled")
async def pled_menu(message: types.Message,state: FSMContext):
    await message.answer(f"Тесты Fotopled, {LEXICON_RU['exit']}",reply_markup=pled_markup)
    time.sleep(1)
    await state.set_state("add_pled")
   

# ------------------------Fotopled tests BLOCK  ----------------------------------
@dp.message_handler(state="add_pled", content_types=["text"])
async def pled_Tgtest(message: types.Message, state: FSMContext):
    driver = webdriver.Chrome(options=chrome_options)
    now_datetime = datetime.datetime.now()
    data_task = await state.get_data()
    status = message.text
    text = LEXICON_RU[status]
    if status == 'Форма заказа':
        await message.answer(text)
        res = pledrOrder_to_tg(driver, url, test_data, False)
        await bot.send_photo(message.chat.id, open(f'{res[-1]}',"rb"),caption=res[:-1])
    elif status == 'Форма заказа + заказ':
        await message.answer(text)
        res = pledrOrder_to_tg(driver, url, test_data, True)
        await bot.send_photo(message.chat.id, open(f'{res[-1]}',"rb"),caption=res[:-1])
    elif status == 'Редактор':
        await message.answer(text)
        res = pledConstr_to_tg(driver, url, test_data, False)
        await message.answer(res) 
    elif status == 'Редактор + заказ':
        await message.answer(text)
        res = pledConstr_to_tg(driver, url, test_data, True)
        await message.answer(res)
    elif status == 'Редактор Cosuv':
        await message.answer(text)
        res = pledCosuv_to_tg(driver, url, test_data, False)
        await message.answer(res)
    elif status == 'Редактор Cosuv + заказ':
        await message.answer(text)
        res = pledCosuv_to_tg(driver, url, test_data, True)
        await message.answer(res)
    else: 
        text = LEXICON_RU['error']             
        print(text)
        await message.answer(text,reply_markup=ReplyKeyboardRemove)
    logging.info(res)

