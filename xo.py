def greet():
    print("Добро пожаловать в игру: ")
    print("     КРЕСТИКИ НОЛИКИ     ")
    print("-------------------------")
    print("   Для совершения хода   ")
    print("  введите две координаты ")
    print("-------------------------")
    print("      Желаю удачи!       ")


def show():
    print()
    print(f"   | 0 | 1 | 2 |")
    print("________________")
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print("________________")
    print()


def asc():
    while True:

        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print("Введите две координаты")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапозона")
            continue

        if field[x][y] != " ":
            print("Клетка занята!")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 0), (1, 0), (2, 0)),
                ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2))
                )
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])

        if symbols == ["X", "X", "X"]:
            print("Выиграл КРЕСТИК!!")
            return True

        if symbols == ["O", "O", "O"]:
            print("Выиграл НОЛИК!!")
            return True
    return False


greet()

field = [[" "] * 3 for i in range(3)]

num = 0
while True:

    num += 1
    show()

    if num % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = asc()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if check_win():
        show()
        break

    if num == 9:
        show()
        print("Победила ДРУЖБА!")
        break