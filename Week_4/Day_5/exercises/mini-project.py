row1 = '[1][2][3]'
row2 = '[4][5][6]'
row3 = '[7][8][9]'

turn = 1

status = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9'
}


def make_board():
    print(row1)
    print(row2)
    print(row3)


def take_move_num():
    if turn % 2 != 0:
        play_num = input("Turn: X. Enter where you want to make your move: ")
        status[int(play_num)] = 'X'
    else:
        play_num = input("Turn: Y. Enter where you want to make your move: ")
        status[int(play_num)] = 'Y'

    return play_num


def take_move_sign():
    if turn % 2 != 0:
        sign = 'X'
    else:
        sign = 'Y'

    return sign


def update_row(play_num, sign):
    num = int(play_num)
    if 1 <= num <= 3:
        row = row1
    elif 4 <= num <= 6:
        row = row2
    else:
        row = row3

    num = str(play_num)
    row = list(row)
    pos = row.index(num)
    row[pos] = sign
    new_row = ''
    for elem in row:
        new_row += elem
    row = new_row
    return row


def change_defined_row(move_num, row):
    global row1
    global row2
    global row3
    if '1' in move_num or '2' in move_num or '3' in move_num:
        row1 = row

    elif '4' in move_num or '5' in move_num or '6' in move_num:
        row2 = row
    else:
        row3 = row

    make_board()


def check_winner():
    if status[1] == status[2] and status[2] == status[3]:
        if status[1] == 'X':
            print("X wins!")
            return True
        else:
            print("Y wins!")
            return True
    elif status[4] == status[5] and status[5] == status[6]:
        if status[4] == 'X':
            print("X wins!")
            return True
        else:
            print("Y wins!")
            return True
    elif status[7] == status[8] and status[8] == status[9]:
        if status[7] == 'X':
            print("X wins!")
            return True
        else:
            print("Y wins!")
            return True
    elif status[1] == status[4] and status[4] == status[7]:
        if status[1] == 'X':
            print("X wins!")
            return True
        else:
            print("Y wins!")
            return True
    elif status[2] == status[5] and status[5] == status[8]:
        if status[2] == 'X':
            print("X wins!")
            return True
        else:
            print("Y wins!")
            return True
    elif status[3] == status[6] and status[6] == status[9]:
        if status[3] == 'X':
            print("X wins!")
            return True
        else:
            print("Y wins!")
            return True
    elif status[1] == status[5] and status[5] == status[9]:
        if status[1] == 'X':
            print("X wins!")
            return True
        else:
            print("Y wins!")
            return True
    elif status[3] == status[5] and status[5] == status[7]:
        if status[3] == 'X':
            print("X wins!")
            return True
        else:
            print("Y wins!")
            return True
    else:
        return False


def play():
    global turn
    make_board()
    while True:
        move_num = take_move_num()
        sign = take_move_sign()
        new_row = update_row(move_num, sign)
        change_defined_row(move_num, new_row)
        check = check_winner()
        if check == True:
            break
        turn += 1
        if turn == 10:
            print("Tie!")
            break


play()
