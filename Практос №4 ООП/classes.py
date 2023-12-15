from main import *
import sqlite3
from defs import *
import time

class CreateDatabase:
    def __init__():
        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
            ID_User INTEGER PRIMARY KEY NOT NULL,
            Username VARCHAR(20) DEFAULT Uncown_user,
            Login TEXT NOT NULL,
            Password TEXT NOT NULL,
            Role VARCHAR(20) NOT NULL
            )
            ''') #! CСОЗДАНИЕ ТАБЛИЦЫ USERS
        
        if has_value_in_column(cursor, 'Users', 'Username', 'First'):
            pass
        else:
            new_user("First", "RamKa", "Basko", "First-admin")
        connection.commit()