import logging
import datetime
import aiogram.utils.markdown as md

from selenium import webdriver
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from loader import dp, admin, bot
from utils.printToTg import printOrder_to_tg, printFlagconstr_to_tg, printCosuv_to_tg, printPlatki_to_tg, printConstr_to_tg
from config_data.config_one_test import url, test_data, foto_url, chrome_options
from keyboards.print_buttons import print_markup
from lexicon.lexicon_ru import LEXICON_RU

logging.basicConfig(level=logging.INFO)


@dp.message_handler(lambda x: int(x.from_user.id) in admin, state="print")
async def print_menu(message: types.Message,state: FSMContext):
    await message.answer("Тесты принтнаткани, команда Выход для возврата",reply_markup=print_markup)
    await state.set_state('add_print')
   

# ------------------------Printnatkani tests BLOCK  ----------------------------------
@dp.message_handler(state="add_print", content_types=["text"])
async def create_test(message: types.Message, state: FSMContext):
    driver = webdriver.Chrome(options=chrome_options)
    now_datetime = datetime.datetime.now()
    data_task = await state.get_data()
    status = message.text
    text = LEXICON_RU[status]
    if status == 'Форма заказа':
        await message.answer(text)
        res = printOrder_to_tg(driver, url, test_data, False)
        await message.answer(res)
    elif status == 'Форма заказа + заказ':
        await message.answer(text)
        res = printOrder_to_tg(driver, url, test_data, True)
        await message.answer(res)
    elif status == 'Флаг-расчет':
        await message.answer(text)
        res = printFlagconstr_to_tg(driver, url, test_data, False)
        await message.answer(res)
    elif status == 'Флаг-расчет + заказ':
        await message.answer(text)
        res = printFlagconstr_to_tg(driver, url, test_data, True)
        await message.answer(res)
    elif status == 'Платки-расчет':
        await message.answer(text)
        res = printPlatki_to_tg(driver, url, test_data, False)
        await bot.send_photo(message.chat.id, open(f'{res[-1]}',"rb"),caption=res[:-1])
    elif status == 'Платки-расчет + заказ':
        await message.answer(text)
        res = printPlatki_to_tg(driver, url, test_data, True)
        await bot.send_photo(message.chat.id, open(f'{res[-1]}',"rb"),caption=res[:-1])
    elif status == 'Редактор':
        await message.answer(text)
        res= printConstr_to_tg(driver, url, test_data, False)
        await message.answer(res)
    elif status == 'Редактор + заказ':
        await message.answer(text)
        res = printConstr_to_tg(driver, url, test_data, True)
        await message.answer(res)
    elif status == 'Редактор Cosuv':
        res = printCosuv_to_tg(driver, url, test_data, False)
        await bot.send_photo(message.chat.id, open(f'{res[-1]}',"rb"),caption=res[:-1])
    elif status == 'Редактор Cosuv + заказ':
        res = printCosuv_to_tg(driver, url, test_data, True)
        await bot.send_photo(message.chat.id, open(f'{res[-1]}',"rb"),caption=res[:-1])
    else: 
        text = LEXICON_RU['error']             
        print(text)
        await message.answer(text)
    logging.info(res)

   
   
