from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Напоминания')],
    [KeyboardButton(text='Оповещения')],
    [KeyboardButton(text='Дневник продуктивности'), KeyboardButton(text='Просмотр записей дневника')],
    [KeyboardButton(text='Трекер времени')],
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')

notify_keyb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ежедневные напоминания', callback_data='daily_notify')],
    [InlineKeyboardButton(text='Кастомные напоминания', callback_data='custom_notify')]
])

help_keyb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Информация о боте', callback_data='bot_info')],
    [InlineKeyboardButton(text='О нас', callback_data='faq')],
    [InlineKeyboardButton(text='Подробнее про функционал', callback_data='functionality')]
])

motivation_keyb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Включить рассылку', callback_data='on_message')],
    [InlineKeyboardButton(text='Выключить рассылку', callback_data='off_message')]
])

date_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Выбрать дату', callback_data='choose_date')]
])

stop_tracking = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Завершить отслеживание', callback_data='stop_tracking')]
])