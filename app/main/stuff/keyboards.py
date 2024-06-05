from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

# Основное меню (ReplyKeyboardMarkup)
main = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text='Дневник продуктивности'),
            KeyboardButton(text='Просмотр записей дневника')
        ],
        [
            KeyboardButton(text='Трекер времени'),
            KeyboardButton(text='Просмотр ваших активностей')
        ]
    ],
    resize_keyboard=True, input_field_placeholder='Выберите пункт меню...'
)




# Кнопки для информации о боте (InlineKeyboardMarkup)
help_keyb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Информация о боте', callback_data='bot_info')
        ],
        [
            InlineKeyboardButton(text='О нас', callback_data='faq')
        ],
        [
            InlineKeyboardButton(text='Подробнее про функционал', callback_data='functionality')
        ]
    ]
)



# Кнопки для выбора даты (InlineKeyboardMarkup)
date_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Выбрать дату', callback_data='choose_date')
        ]
    ]
)

# Кнопки для завершения отслеживания (InlineKeyboardMarkup)
stop_tracking = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Завершить отслеживание', callback_data='stop_tracking')
        ]
    ]
)
