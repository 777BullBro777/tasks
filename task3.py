# напишите функцию поиска наименьшего из 3 введенных чисел

def search(num1, num2, num3):
    try:
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
    except ValueError:
        print("Ошибка! Ввод нечисловых данных!")
        exit()
    else:
        if num1 < num2 and num1 < num3:
            print(num1, " <---Наименьшее число!")
        elif num2 < num1 and num2 < num3:
            print(num2, " <---Наименьшее число!")
        else:
            print(num3, " <---Наименьшее число!")

if __name__ == '__main__':
    num1 = input("Введите целое число : ")
    num2 = input("Введите целое число : ")
    num3 = input("Введите целое число : ")
    search(num1, num2, num3)
