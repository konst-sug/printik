from aiogram import types  

print_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
          [
            types.KeyboardButton(text="Форма заказа"),
            types.KeyboardButton(text="Форма заказа + заказ")
        ], [
            types.KeyboardButton(text="Флаг-расчет"),
            types.KeyboardButton(text="Флаг-расчет + заказ")
        ], [
            types.KeyboardButton(text="Платки-расчет"),
            types.KeyboardButton(text="Платки-расчет + заказ")
        ], [
            types.KeyboardButton(text="Редактор "),
            types.KeyboardButton(text="Редактор + заказ")
        ],[
            types.KeyboardButton(text="Редактор Cosuv"),
            types.KeyboardButton(text="Редактор Cosuv + заказ")
        ],[
            types.KeyboardButton(text="Выход")
        ]
        
    ])