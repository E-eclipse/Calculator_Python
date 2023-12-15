import sqlite3 as sq


conn = sq.connect("base.db")

cursor = conn.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               age INTEGER NOT NULL,
               email TEXT NOT NULL
        )
""")

cursor.execute('INSERT INTO users (name, age, email) VALUES ("Иван", "2", "ivan2021@mpt.com")')

conn.commit()

# cursor.execute("DROP TABLE IF EXISTS users")