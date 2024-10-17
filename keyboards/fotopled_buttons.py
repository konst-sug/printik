from aiogram import types  

pled_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
          [
            types.KeyboardButton(text="Форма заказа"),
            types.KeyboardButton(text="Форма заказа + заказ")
        ], [
            types.KeyboardButton(text="Редактор"),
            types.KeyboardButton(text="Редактор + заказ")
        ], [
            types.KeyboardButton(text="Редактор Cosuv"),
            types.KeyboardButton(text="Редактор Cosuv + заказ")
        ], [
            types.KeyboardButton(text="Выход")
        ]
    ])