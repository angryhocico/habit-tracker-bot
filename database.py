import sqlite3

def init_db():
    with sqlite3.connect("habit_bot.db") as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE NOT NULL,
            username TEXT,
            joined_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT NOT NULL,
            description TEXT,
            FOREIGN KEY(user_id) REFERENCES users(telegram_id)
        )
        """)
        conn.commit()

def add_user(telegram_id: int, username: str):
    with sqlite3.connect("habit_bot.db") as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (telegram_id, username) VALUES (?, ?)", 
                (telegram_id, username)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False