# напишите функцию переводчик км/ч в м/с
def translater(speed):
    speed = int(input("Введите значение км/ч :  "))
    print("Перевод завершён!\nОтвет : ", (speed * 1000) / 3600, "м/с")
if __name__ == '__main__':
    translater(speed)
