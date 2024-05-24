import telebot
from base.base import init_db, has_been_greeted, set_greeted

API_TOKEN = '6547786362:AAGkPf5yL_cUcQK0MIDxNy46PJiLINsiBUo'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def greet_new_user(message):
    chat_id = message.chat.id
    if not has_been_greeted(chat_id):
        bot.reply_to(message, 'Привет, я твой бот-помощник, я помогу'
                              ' тебе поднять твою продуктивность и организовать день!\n')
        set_greeted(chat_id)
    else:
        bot.reply_to(message, message.text)

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 'Мой функционал:\n'
                          '\tДневник\n'
                          '\тНапоминания\n'
                          '\тСписок дел\n'
                          'Надеюсь, я буду вам полезен.')

if __name__ == '__main__':
    init_db()
    bot.infinity_polling()

