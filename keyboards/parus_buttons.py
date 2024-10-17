from aiogram import types  

parus_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
          [
            types.KeyboardButton(text="Форма заказа"),
            types.KeyboardButton(text="Форма заказа + заказ")
        ], [
            types.KeyboardButton(text="Флаг-расчет"),
            types.KeyboardButton(text="Флаг-расчет + заказ")
        ], [
            types.KeyboardButton(text="Флаг-продукция"),
            types.KeyboardButton(text="Флаг-продукция + заказ")
        ],[
            types.KeyboardButton(text="Редактор Cosuv"),
            types.KeyboardButton(text="Редактор Cosuv + заказ")
        ], [
            types.KeyboardButton(text="Выход")
        ]
    ])