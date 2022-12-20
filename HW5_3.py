# Создайте программу для игры в ""Крестики-нолики""

from random import randint


def our_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)


def go_X(move):
    i = False
    while i == False:
        if not move:
            a = int(
                input(f"{first_player}, куда поставишь крестик? "))
        else:
            a = int(
                input(f"{second_player}, куда поставишь крестик? "))
        while a < 0 or a > 9:
            a = int(
                input("Ты ввел некорректное число, попробуй еще раз"))
        if (str(board[a-1]) not in "xo"):
            board[a-1] = "x"
            i = True
        else:
            print("Эта клетка уже занята!")


def go_0(move):
    i = False
    while i == False:
        if not move:
            a = int(
                input(f"{first_player}, куда поставишь нолик? "))
        else:
            a = int(
                input(f"{second_player}, куда поставишь нолик? "))
        while a < 0 or a > 9:
            a = int(
                input("Ты ввел некорректное число, попробуй еще раз"))
        if (str(board[a-1]) not in "xo"):
            board[a-1] = "o"
            i = True
        else:
            print("Эта клетка уже занята!")


def win(board):
    winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
               (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in winners:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return True
    return False


print("Сейчас будем играть в крестики-нолики!")

first_player = input("Первый игрок, пожалуйста, представься ")
second_player = input("Второй игрок, пожалуйста, представься ")

print("Вот наше поле: ")
board = list(range(1, 10))
our_board(board)

player_number = randint(0, 1)

if player_number == 0:
    a = print(f"{first_player}, ты ходишь первым и играешь крестиками ")
    move = False
else:
    a = print(f"{second_player}, ты ходишь первым и играешь крестиками ")
    move = True

go_X(move)
our_board(board)
move = not move

for i in range(4):
    if win(board) == False:
        go_0(move)
        our_board(board)
        move = not move
    if win(board) == False:
        go_X(move)
        our_board(board)
        move = not move
    else:
        if move:
            print(f"{first_player}, ты победил! Поздравляю! ")
            break
        else:
            print(f"{second_player}, ты победил! Поздравляю! ")
            break
