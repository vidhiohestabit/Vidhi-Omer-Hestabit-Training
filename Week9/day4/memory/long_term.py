import sqlite3
import os
DB_PATH = "memory/long_term.db"


class LongTermMemory:
    def __init__(self):
        self._init_db()

    def _init_db(self):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT,
            category TEXT
        )
        """)

        conn.commit()
        conn.close()

    def store(self, text, category="general"):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO memory (content, category) VALUES (?, ?)",
            (text, category)
        )

        conn.commit()
        conn.close()

    def retrieve_all(self):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute("SELECT content FROM memory")
        rows = cur.fetchall()

        conn.close()

        return [r[0] for r in rows]