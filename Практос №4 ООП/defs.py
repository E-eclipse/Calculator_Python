from classes import *
import sqlite3
from main import *
import time


def clear_screen():
    print("\033[H\033[J")


def new_user(Username, Login, Password, Role="User"):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (Username, Login, Password, Role) VALUES (?, ?, ?, ?)', (Username, Login, Password, Role))
    connection.commit()
    