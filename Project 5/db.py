import sqlite3
import os

DB_NAME = "chat_memory.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS chats (
            session_id TEXT,
            role TEXT,
            content TEXT
        )''')

def save_chat(session_id, role, content):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO chats VALUES (?, ?, ?)", (session_id, role, content))

def get_chat_history(session_id):
    with sqlite3.connect(DB_NAME) as conn:
        rows = conn.execute("SELECT role, content FROM chats WHERE session_id = ?", (session_id,)).fetchall()
        return rows

def list_sessions():
    with sqlite3.connect(DB_NAME) as conn:
        rows = conn.execute("SELECT DISTINCT session_id FROM chats").fetchall()
        return [r[0] for r in rows]
