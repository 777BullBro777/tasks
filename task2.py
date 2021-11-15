# напишите функцию переводчик км/ч в м/с
def translater(speed):
    speed1 = (speed * 1000) / 3600
    print("Перевод завершён!\nОтвет : ", speed1, "м/с")
if __name__ == '__main__':
    speed = int(input("Введите значение км/ч :  "))
    translater(speed)
