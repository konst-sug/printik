from aiogram import types


kaz_markup =  types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
          [
            types.KeyboardButton(text="Форма заказа"),
            types.KeyboardButton(text="Форма заказа + заказ")
        ], [
            types.KeyboardButton(text="Редактор "),
            types.KeyboardButton(text="Редактор + заказ")
        ], [
            types.KeyboardButton(text="Выход") 
        ]
    ])