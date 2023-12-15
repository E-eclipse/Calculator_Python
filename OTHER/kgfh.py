from math import *
print("Выберете необходимую операцию:\n1) Сложение\n2) Вычитание\n3) Умножение\n4) Деление\n5) Возведение в степень\n6) Квадратный корень\n7) Факториал\n8) Синус\n9) Косинус\n")

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
        a, b = int(input()), int(input())
        flag = False
    elif operation == 5:
        print("Введите сначала число, а потом степень: ")
        a, b = int(input()), int(input())
        flag = False
    elif operation >= 6 and operation <= 9:
        print("Введите число: ")
        a = int(input())
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
        print(a, "/", b, "= ", a / b)
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
    case _:
        pass