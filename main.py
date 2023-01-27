field = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']
         ]


def show_field(f):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i) + ' ' + ' '.join(field[i]))


def users_input(f):
    while True:
        place = input('Введите координаты:').split()
        if len(place) != 2:
            print('Введите две координаты')
            continue
        if not (place[0].isdigit() and place[1].isdigit()):
            print('Координаты должны быть положительными числами. Введите числа')
            continue
        x, y = map(int, place)
        if not (0 <= x < 3 and 0 <= y < 3):
            print('Координаты вышли за границы поля')
            continue
        if f[x][y] != '-':
            print('Клетка занята')
            continue
        break
    return x, y

def win_1(f, user):
    def check_line(a1, a2, a3, user):
        if a1 == user and a2 == user and a3 == user:
            return True

    for n in range(3):
        if check_line(f[n][0], f[n][1], f[n][2], user) or \
                check_line(f[0][n], f[1][n], f[2][n], user) or \
                check_line(f[0][0], f[1][1], f[2][2], user) or \
                check_line(f[2][0], f[1][1], f[0][2], user):
            return True
    return False

while True:
    var = input('Выберите кто ходит певрым: x или o: ')
    if var == 'x':
        count = 0
        break
    elif var =='o':
        count = 1
        break
    else:
        print('Введите х или о')
        continue



while True:
    print(f'Ход {count};')
    if count % 2 == 0:
        print('Очередь крестиков;')
        user = 'x'
    else:
        print('Очередь ноликов;')
        user = 'o'
    show_field(field)
    x, y = users_input(field)
    field[x][y] = user
    if count == 9 or (count == 8 and user == 'x'):
        print('Ничья')
        show_field(field)
        break
    if win_1(field, user):
        print(f'Выйграл {user}')
        show_field(field)
        break
    count += 1




