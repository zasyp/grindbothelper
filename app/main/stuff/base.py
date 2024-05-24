import sqlite3

# Инициализация базы данных
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_greetings (
        chat_id INTEGER PRIMARY KEY
    )
    ''')
    conn.commit()
    conn.close()

# Проверка, отправлялось ли приветственное сообщение
def has_been_greeted(chat_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT chat_id FROM user_greetings WHERE chat_id = ?', (chat_id,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

# Сохранение информации о пользователе
def set_greeted(chat_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_greetings (chat_id) VALUES (?)', (chat_id,))
    conn.commit()
    conn.close()
