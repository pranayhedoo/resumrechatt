import sqlite3
import datetime

conn = sqlite3.connect("chat_history.db", check_same_thread=False)
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS chats (session TEXT, message TEXT, response TEXT, timestamp TEXT)""")

def save_chat(session, message, response):
    c.execute("INSERT INTO chats VALUES (?, ?, ?, ?)", (session, message, response, str(datetime.datetime.now())))
    conn.commit()

def get_chat_history(session):
    c.execute("SELECT message, response FROM chats WHERE session=? ORDER BY timestamp", (session,))
    return c.fetchall()

def list_sessions():
    c.execute("SELECT DISTINCT session FROM chats ORDER BY timestamp DESC")
    return [row[0] for row in c.fetchall()]
