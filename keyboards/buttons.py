from aiogram import types


markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(types.KeyboardButton("Тесты"))
markup.add(types.KeyboardButton("Назад"))