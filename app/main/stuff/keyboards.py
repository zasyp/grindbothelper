from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Напоминания')],
                                     [KeyboardButton(text='Оповещения')],
                                     [KeyboardButton(text='Дневник продуктивности'),
                                      KeyboardButton(text='Прогресс по целям')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')

notify = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ежедневные напоминания', callback_data= 'daily_notify')],
    [InlineKeyboardButton(text='Кастомные напоминания', callback_data= 'custom_notify')]])


help_keyb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Информация о боте', callback_data= 'bot_info')],
    [InlineKeyboardButton(text='О нас', callback_data= 'faq')]])