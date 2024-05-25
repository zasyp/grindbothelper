from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Напоминания')],
                                     [KeyboardButton(text='Оповещения')],
                                     [KeyboardButton(text='Дневник продуктивности'),
                                      KeyboardButton(text='Прогресс по целям')]])

help_keyb = KeyboardButton