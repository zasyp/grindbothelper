import telebot
from base import has_been_greeted, set_greeted

API_TOKEN = '6547786362:AAGkPf5yL_cUcQK0MIDxNy46PJiLINsiBUo'

bot = telebot.TeleBot(API_TOKEN)

def greet_user(message):
    chat_id = message.chat.id
    bot.reply_to(message, 'Привет, я твой бот-помощник, я помогу'
                          ' тебе поднять твою продуктивность и организовать день!\n')
    set_greeted(chat_id)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    greet_user(message)

# Обработчик для новых сообщений
@bot.message_handler(func=lambda message: True)
def greet_new_user(message):
    chat_id = message.chat.id
    if not has_been_greeted(chat_id):
        greet_user(message)
    else:
        bot.reply_to(message, message.text)

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 'Мой функционал:\n'
                          '\tДневник\n'
                          '\тНапоминания\n'
                          '\тСписок дел\n'
                          'Надеюсь, я буду вам полезен.')