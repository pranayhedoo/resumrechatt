import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("chat_memory.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS chats (
        id TEXT PRIMARY KEY,
        session_id TEXT,
        role TEXT,
        message TEXT,
        timestamp DATETIME,
        session_summary TEXT,
        last_updated DATETIME
    )''')
    conn.commit()
    conn.close() 

def save_chat(session_id, role, message):
    conn = sqlite3.connect("chat_memory.db")
    c = conn.cursor()
    now = datetime.now()
    c.execute('''INSERT INTO chats VALUES (?, ?, ?, ?, ?, ?, ?)''',
              (str(now.timestamp()), session_id, role, message, now, "", now))
    conn.commit()
    conn.close()

def get_chat_history(session_id):
    conn = sqlite3.connect("chat_memory.db")
    c = conn.cursor()
    c.execute('SELECT role, message FROM chats WHERE session_id = ? ORDER BY timestamp', (session_id,))
    data = c.fetchall()
    conn.close()
    return data

def list_sessions():
    conn = sqlite3.connect("chat_memory.db")
    c = conn.cursor()
    c.execute('SELECT DISTINCT session_id FROM chats ORDER BY last_updated DESC')
    sessions = [row[0] for row in c.fetchall()]
    conn.close()
    return sessions
