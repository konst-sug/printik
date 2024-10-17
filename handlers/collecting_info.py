import logging
import datetime

from aiogram import types
from aiogram.types import Message
from loader import dp,query,bot,admin
from aiogram.dispatcher.storage import FSMContext
from config_data.config_one_test import foto_url, db_path
from database.sqliter import SQLiter
from lexicon.lexicon_ru import LEXICON_RU

db = SQLiter(db_path)
user_info = {}

async def formating_time(obj):
    if obj[0] == "0" and obj[1] == "0":
        obj = 0
        return obj
    elif obj[0] == "0":
        obj = int(obj[1])
        return obj
    else:
        obj = int(obj)
        return obj


# @dp.message_handler(lambda x: int(x.from_user.id), regexp="Сброс", state="*")
# @dp.message_handler(commands=["cancel"],state='*')
# @dp.message_handler(commands=["start"],state="close_waybill_mileage")
# @dp.message_handler(commands=["start"],state="close_waybill")
# @dp.message_handler(commands=["start"],state="admin")
# @dp.message_handler(commands=["start"],state="del_user")
# @dp.message_handler(commands=["start"],state="add_user")
# @dp.message_handler(commands=["start"],state="auto_number")
# @dp.message_handler(commands=["start"],state="fio")
# @dp.message_handler(commands=["start"],state="desired_time")
# @dp.message_handler(commands=["start"],state="mileage")
# @dp.message_handler(commands=["start"])
# async def hello_text(message: types.Message,state: FSMContext):
#     await state.reset_state(with_data=True)
#     text = 'Вы находитесь в главном меню Print_test_bot!'
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(types.KeyboardButton("Создать новый путевой лист"))
#     markup.add(types.KeyboardButton("Закрыть путевой лист"))
#     markup.add(types.KeyboardButton("Сброс"))
#     await message.answer(text,reply_markup=markup)
#     await bot.send_photo(message.chat.id, open(foto_url,"rb"), caption=text)
#     hello_text = LEXICON_RU['/start']
#     await message.answer(text=hello_text,parse_mode=types.ParseMode.HTML)


@dp.message_handler(commands=["start"])
@dp.message_handler(lambda x: int(x.from_user.id), regexp="Сброс", state="*")
@dp.message_handler(commands=["cancel"],state='*')
@dp.message_handler(commands=["start"],state="print")
@dp.message_handler(commands=["start"],state="winder")
@dp.message_handler(commands=["start"],state="admin")
@dp.message_handler(commands=["start"],state="pled")
@dp.message_handler(commands=["start"],state="kaz")
@dp.message_handler(commands=["start"],state="parus")
@dp.message_handler(commands=["start"],state="statistics")
@dp.message_handler(commands=["start"],state="local")
@dp.message_handler(commands=["start"],state="view")
async def hello_text(message: types.Message,state: FSMContext):
    await state.reset_state(with_data=True)
    text = 'Вы находитесь в главном меню Print_test_bot!'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Тесты сайтов"))
    #markup.add(types.KeyboardButton("Info"))
    await bot.send_photo(message.chat.id, open(foto_url,"rb"), caption=text)
    hello_text = LEXICON_RU['/start']
    await message.answer(text=hello_text,parse_mode=types.ParseMode.HTML, reply_markup=markup)
    user_id = message.from_user.id
    user_name = message.from_user.username
    start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user_info = {
        "tg_id" : user_id,
        "user_name" : message.from_user.username,
        "start_time" : datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    logging.info(user_info)
    res = db.user_exists(user_id)
    if res:
        logging.info('user_exits')
        db.save_user_entry(user_id, user_name, start_time)
    else:
        logging.info('user_not_exits')
        db.save_user(user_id, user_name, start_time)
    await state.update_data(user_id=user_id)  
    

 
@dp.message_handler(commands=["help"],state='*')
async def help_text(message: types.Message,state: FSMContext):
    await state.reset_state(with_data=True)
    text = LEXICON_RU['/help']
    await message.answer(text=text, parse_mode=types.ParseMode.HTML)


@dp.message_handler(state='*', regexp="Тесты сайтов")
async def info_print(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user_id  = data["user_id"]
    print(user_id)
    if user_id in admin:
        await message.answer(f"{LEXICON_RU['entry']}",reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer(f"{LEXICON_RU['no_entry']}",reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state='*', regexp="Info")
async def info_print(message: types.Message, state: FSMContext):
    print("Тесты")
    await message.answer(f"{LEXICON_RU['test']}",reply_markup=types.ReplyKeyboardRemove())  


@dp.message_handler(lambda x: int(x.from_user.id) not in admin,commands=["cancel"], state="*")
async def back_to_start(message: types.Message, state: FSMContext):
    text = "Выход в начало/ Cancelled."
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    await state.reset_state()
    await hello_text(message, state)   