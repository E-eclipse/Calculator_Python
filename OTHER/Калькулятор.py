from math import *
from art import tprint

tprint("--------Calculator---------")
print("Выберете необходимую операцию:")
print("1.  Сложение")
print("2.  Вычитание")
print("3.  Умножение")
print("4.  Деление")
print("5.  Возведение в степень")
print("6.  Квадратный корень")
print("7.  Факториал")
print("8.  Синус")
print("9.  Косинус")
print("10. Тангенс\n")

flag = True

while flag == True:
    while True:
        try:
            operation = int(input())
            break
        except ValueError:
            print("Неправильно, попробуйте снова")


    if operation >= 1 and operation <= 4:
        print("Введите 2 числа: ")
        a, b = float(input()), float(input())
        flag = False
    elif operation == 5:
        print("Введите сначала число, а потом степень: ")
        a, b = float(input()), float(input())
        flag = False
    elif operation >= 6 and operation <= 10:
        print("Введите число: ")
        a = float(input())
        flag = False
    else:
        print("Попробуйте еще раз\n")

match operation:
    case 1:
        print(a, "+", b, "= ", a + b)
    case 2:
        print(a, "-", b, "= ", a - b)
    case 3:
        print(a, "*", b, "= ", a * b)
    case 4:
        if b != 0:
            print(a, "/", b, "= ", a / b)
        else:
            print("На ноль делить нельзя!")
    case 5:
        print(a, "в степени ", b, "= ", a**b)
    case 6:
        print("Корень из", a, "= ", sqrt(a))
    case 7:
        print("Факториал от", a, "= ", factorial(a))
    case 8:
        print("sin", a, "=", sin(a))
    case 9:
        print("cos", a, "=", cos(a))
    case 10:
        print("tg", a, "=", tan(a))