# board[0 + i * 3], board[1 + i * 3], board[2 + i * 3]
# Создать игру крестики-нолики
#                                   ПЛАН
#                               Отрисовка поля   +
#                           Создание функции хода игрока   +
#                               Обработка исключений        +
#                                 Параметры победы          +
#                                   Сам цикл игры           в процессе


def draw_board():
    print('--------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('--------------')


def take_input(token):
    while True:
        answer = input("Введите позицию куда поставить " + token + "? : ")
        if not (answer in "123456789"):
            print("Ошибка!")
            continue
        answer = int(answer)
        if str(board[answer - 1]) in "XO":
            print("Ошибка! Клетка занята")
            continue
        board[answer - 1] = token
        break


def check_win():
    for n in wins_combinations:
        if board[n[0] - 1] == board[n[1] - 1] == board[n[2] - 1]:
            return board[n[1] - 1]
        else:
            return False


if __name__ == '__main__':
    wins_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    board = list(range(1, 10))
    draw_board()
    move = 0  # ход игрока
    while True:
        draw_board()
        if move % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        if move > 3:
            check = check_win()
            if check == check_win():
                draw_board()
                print("Вы выйграли!")
                break
        move += 1
        if move > 8:
            draw_board()
            print("Ничья!")
            break
