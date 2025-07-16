import sqlite3

def save_chat(query, response):
    conn = sqlite3.connect("chat_history.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS chats (question TEXT, answer TEXT)''')
    c.execute("INSERT INTO chats VALUES (?, ?)", (query, response))
    conn.commit()
    conn.close()

def load_chat():
    conn = sqlite3.connect("chat_history.db")
    c = conn.cursor()
    c.execute("SELECT * FROM chats")
    data = c.fetchall()
    conn.close()
    return data
