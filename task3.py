# напишите функцию поиска наименьшего из 3 введенных чисел
def search(num1, num2, num3):
    num1 = int(input("Введите целое число : "))
    num2 = int(input("Введите целое число : "))
    num3 = int(input("Введите целое число : "))
    if num1 < num2 and num1 < num3:
        print(num1, "Наименьшее число!")
    elif num2 < num1 and num2 < num3:
        print(num1, "Наименьшее число!")
    else:
        print(num3, "Наименьшее число!")
if __name__ == '__main__':
    search(num1, num2, num3)

