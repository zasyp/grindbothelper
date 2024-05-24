import telebot
from base import init_db
from handlers import bot  # Импортируем объект бота из stuff.py

if __name__ == '__main__':
    init_db()  # Инициализация базы данных
    bot.infinity_polling()  # Запуск бота