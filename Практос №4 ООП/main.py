from classes import *
import sqlite3
from defs import *
import time




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


def clear_screen():
    print("\033[H\033[J")

def get_choice(options):
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    choice = input("Выберите вариант: ")
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
        choice = input("Пожалуйста, выберите номер варианта: ")
    return int(choice)

def has_value_in_column(cursor, table, column, value):
    query = 'SELECT 1 from {} WHERE {} = ? LIMIT 1'.format(table, column)
    return cursor.execute(query, (value,)).fetchone() is not None


def close_connection():
    connection.commit()
    connection.close()

def new_user(Username, Login, Password, Role="User"):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (Username, Login, Password, Role) VALUES (?, ?, ?, ?)', (Username, Login, Password, Role))
    connection.commit()
    

if has_value_in_column(cursor, 'Users', 'Username', 'First'):
    pass
else:
    new_user("First", "RamKa", "Basko", "First-admin")
connection.commit()


def reg():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    a = True
    while a == True:
        clear_screen()
        print("Для продолжения вам необходимо войти")
        b = True
        while b:
            nickname = input("Введите свое имя пользователя: ")
            if has_value_in_column(cursor, 'Users', 'Username', nickname):
                c = True
                while c:
                    User_login = (cursor.execute("SELECT * FROM Users WHERE Username = '{}'".format(nickname)).fetchone())[2]
                    User_password = (cursor.execute("SELECT * FROM Users WHERE Username = '{}'".format(nickname)).fetchone())[3]
                    Role = (cursor.execute("SELECT * FROM Users WHERE Username = '{}'".format(nickname)).fetchone())[4]
                    print(User_login, User_password)
                    peremennaya = True
                    while peremennaya:
                        login = input("Введите логин: ")
                        password = input("Пароль: ")
                        if login == User_login and password == User_password:
                            print("Вход прошел успешно. Добро пожаловать, " + nickname)
                            peremennaya = False
                            a = False
                        else:
                            print("Неправильный логин или пароль. Попробуйте снова.")
                    c = False
                
                b = False
                a = False
            else:
                print("Такого имени нет, желаете зарегистрироваться?")
                answer = get_choice(["Да", "Нет"])
                if answer == 1:
                    clear_screen()
                    print("                                                                                  Регистрация")
                    z = True
                    while z:
                        nickname = input("Введите новое имя пользователя: ")
                        if has_value_in_column(cursor, 'Users', 'Username',nickname):
                            print("Пользователь с таким именем уже есть. Попробуйте еще раз.")
                        else:
                            z = False
                    h = True
                    while h:
                        login = input("Введите логин: ")
                        password = input("Введите пароль: ")
                        print("Вы уверены, что вы ввели данные правильно?")
                        answer = get_choice(["Да", "Нет"])
                        if answer == 1:
                            Role = "User"
                            connection = sqlite3.connect('users.db')
                            cursor = connection.cursor()
                            new_user(nickname, login, password)
                            print("User added")
                            b = False
                            h = False
                        else:
                            clear_screen()
                            print("Тогда введите данные еще раз")
                            time.sleep(1)
                            clear_screen()

    return nickname, login, password, Role

#! РЕГИСТРАЦИЯ
connection = sqlite3.connect('users.db')
cursor = connection.cursor()

nickname, login, password, Role = reg()


connection.commit()
connection.close()

print(nickname + " " + login + " " + password + " " + Role)
print("Программа завершена")