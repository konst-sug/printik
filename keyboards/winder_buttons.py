from aiogram import types  
winder_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
          [
            types.KeyboardButton(text="Форма заказа"),
            types.KeyboardButton(text="Форма заказа + заказ")
        ], [
            types.KeyboardButton(text="Флаг-расчет"),
            types.KeyboardButton(text="Флаг-расчет + заказ")
        ], [
            types.KeyboardButton(text="Флаг-расчет + заказ2")
        ], [
            types.KeyboardButton(text="Выход") 
        ]
    ])