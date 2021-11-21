# Усложни свой калькулятор. Добавь в него:
# 1. расчёт факториала
# 2. возведение в степень
# 3. модуль
# 4. логарифм (основание тоже вводится)
# 5. рассчет процентного соотношения.
import math

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

def degreed(number, degree):
    print("Ответ : ", number ** degree)
def module(number):
    if number > 0:
        print("| ", number, " | =  ", number)
    elif number == 0:
        print("| ", number, " | =  0")
    elif number < 0:
        print("| ", number, " | =  ", number * (-1))

def log(number, base):
    math.log(number, base)

def procent(array):
    number = None
    kolvo = 0
    array = []
    while number != 0:
        number = float(input("Введите число от 1 до 100 :  "))
        kolvo = +1
        if number == 0:
            array.pop(0)
            kolvo = -1
            result1 = sum(array)
            result2 = 100 / (kolvo * 100)
            print("Ответ : ", result1 * result2, "%")
            break
        if number >= 101:
            print("Ошибка")
            exit()
        elif number <= 100:
            array.append(number)
            print(array)

def isfloat(num1, num2):
    try:
        num1(float)
        num2(float)
        return True
    except ValueError:
        print("Ошибка!", ValueError)
        return False

def simple_operation(x):
    num1 = float(input("Введите первое  число : "))
    zna4 = input(str('Введите знак : '))
    num2 = float(input('Введите второе число : '))
    if zna4 == str("+"):
        x = num1 + num2
        print(x)
    elif zna4 == str("-"):
        x = num1 - num2
        print(x)
    elif zna4 == str("*"):
        x = num1 * num2
        print(x)
    elif zna4 == str("/"):
        try:
            if zna4 == str("/"):
                x = num1 / num2
                num1 = float(num1)
                num2 = float(num2)
        except ZeroDivisionError:
            print(ZeroDivisionError, "Деление на ноль!")
            x = 0
            print(x)
        else:
            print(num1 / num2)

if __name__ == '__main__':
    menu = int(input("Введите операцию :\n1)расчёт факториала\n2)возведение в степень"
                        "\n3)модуль\n4)логарифм\n5)расчёт процентоного соотношения"
                        "\n6)сложение\умножение\вычитание\деление\n7)Выход\nВаш выбор :  "))
    if menu == 1:
        number = int(input("Введите число :  "))
        factorial(number)
        print("Ответ : ", factorial(number))
    elif menu == 2:
        number = int(input("Введите число для возведения его в степень :  "))
        degree = int(input("Введите степень возведения :  "))
        degreed(number, degree)
    elif menu == 3:
        number = int(input("Введите число :  "))
        module(number)
    elif menu == 4:
        number = int(input("Введите число :  "))
        base = int(input("Введите базовое значение :  "))
        print("Ответ : ", log(number, base))
    elif menu == 5:
        number = None
        kolvo = 0
        array = []
        procent(array)
    elif menu == 6:
        x = None
        simple_operation(x)
    elif menu == 7:
        print("Выход из программы!")
        exit()
else:
    print("Ошибка введённого значения! Выход из программы!")
    exit()
