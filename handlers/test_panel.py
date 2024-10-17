import logging
import aiogram.utils.markdown as md

from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from loader import dp, admin, bot
from keyboards.test_buttons import start_markup
from keyboards.buttons import markup
from lexicon.lexicon_ru import LEXICON_RU

logging.basicConfig(level=logging.INFO)

inp_data = dict()
user_data = dict()
object_data = dict()
#db = SQLiter('bd.db')
exlist = []


def check_format(msg):
    try:
        elements = msg.split()
        elements[1]
    except Exception:
        return False
    else:
        if len(elements) > 2:
            return False
        return True


# --------блок управления для администратора --------
@dp.message_handler(lambda x: int(x.from_user.id) in admin, regexp="admin")
@dp.message_handler(lambda x: int(x.from_user.id) in admin, commands=["admin"])
async def admin_menu(message: types.Message,state: FSMContext): 
    await state.reset_state(with_data=True)
    await message.answer("Панель выбора тестов, для сброса использовать команду Выход",reply_markup=start_markup)
    await state.set_state("admin")


@dp.message_handler(state="admin", regexp="Printnatkani")
async def create_print(message: types.Message, state: FSMContext):
    await message.answer(f"{LEXICON_RU['test']} {message.text}",reply_markup=markup)
    await state.set_state("print")
   

@dp.message_handler(state="admin", regexp="Flagwinder")
async def create_winder(message: types.Message, state: FSMContext):
    await message.answer(f"{LEXICON_RU['test']} {message.text}",reply_markup=markup)
    await state.set_state("winder")


@dp.message_handler(state="admin", regexp="Flag-parus")
async def create_parus(message: types.Message, state: FSMContext):
    await message.answer(f"{LEXICON_RU['test']} {message.text}",reply_markup=markup)
    await state.set_state("parus")

    
@dp.message_handler(state="admin", regexp="Fotopled")
async def create_pled(message: types.Message, state: FSMContext):
    await message.answer(f"{LEXICON_RU['test']} {message.text}",reply_markup=markup)
    await state.set_state("pled")


@dp.message_handler(state="admin", regexp="Print-kz")
async def create_kaz(message: types.Message, state: FSMContext):
    await message.answer(f"{LEXICON_RU['test']} {message.text}",reply_markup=markup)
    await state.set_state("kaz")


@dp.message_handler(state="admin", regexp="Statistics")
async def create_stat(message: types.Message, state: FSMContext):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Снимок панели статистики"))
    markup.add(types.KeyboardButton("Сброс"))
    await message.answer(f"{LEXICON_RU['stat']}",reply_markup=markup)
    await state.set_state("local")


@dp.message_handler(lambda x: int(x.from_user.id) in admin, state="*", regexp="Выход")
@dp.message_handler(lambda x: int(x.from_user.id) in admin, state="*", regexp="cancel")
@dp.message_handler(lambda x: int(x.from_user.id) in admin, commands=["cancel"], state="*")
async def back_to_start(message: types.Message, state: FSMContext):
    text = "Выход в тест меню/ Cancelled."
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    await state.reset_state()
    await admin_menu(message, state)


@dp.message_handler(lambda x: int(x.from_user.id) in admin, state="*", regexp="Назад")
async def back_to_admin_menu(message: types.Message, state: FSMContext):
    text = "Возврат в меню тестов"
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    await state.reset_state()
    await admin_menu(message, state)



  