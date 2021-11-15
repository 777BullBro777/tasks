# напишите функцию переводчик км/ч в м/с
def translate(speed1):
    speed1 = (speed * 1000) / 3600
if __name__ == '__main__':
    speed = int(input("Введите значение км/ч :  "))
    print("Перевод завершён!\nОтвет : ", speed1)
