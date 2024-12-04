with open("input_1.txt") as f:
    file = f.read().splitlines()

total = 0


def check_out_of_bounds(ws: list[str], index_1: int, index_2: int) -> bool:
    status = True
    if 0 <= index_1 <= len(ws)-1:
        ()
    else:
        status = False
    if 0 <= index_2 <= len(ws[0])-1:
        ()
    else:
        status = False
    return status

# *
#  \
#   \
#    X

def diag_left(ws: list[str], reverse: bool) -> bool:
    try:
        if ws[i-(-1 if reverse else 1)][j-(-1 if reverse else 1)] != 'M' or check_out_of_bounds(ws, i-(-1 if reverse else 1), j-(-1 if reverse else 1)) is False:
            return False
        if ws[i-(-2 if reverse else 2)][j-(-2 if reverse else 2)] != 'A' or check_out_of_bounds(ws, i-(-2 if reverse else 2), j-(-2 if reverse else 2)) is False:
            return False
        if ws[i-(-3 if reverse else 3)][j-(-3 if reverse else 3)] != 'S' or check_out_of_bounds(ws, i-(-3 if reverse else 3), j-(-3 if reverse else 3)) is False:
            return False
        else:
            return True
    except IndexError:
        return False

#    *
#   /
#  /
# X

def diag_right(ws: list[str], reverse: bool) -> bool:
    try:
        if ws[i-(-1 if reverse else 1)][j-(1 if reverse else -1)] != 'M' or check_out_of_bounds(ws, i-(-1 if reverse else 1), j-(1 if reverse else -1)) is False:
            return False
        if ws[i-(-2 if reverse else 2)][j-(2 if reverse else -2)] != 'A' or check_out_of_bounds(ws, i-(-2 if reverse else 2), j-(2 if reverse else -2)) is False:
            return False
        if ws[i-(-3 if reverse else 3)][j-(3 if reverse else -3)] != 'S' or check_out_of_bounds(ws, i-(-3 if reverse else 3), j-(3 if reverse else -3)) is False:
            return False
        else:
            return True
    except IndexError:
        return False

# *
# |
# |
# X


def upwards(ws: list[str], reverse: bool) -> bool:
    try:
        if ws[i-(-1 if reverse else 1)][j] != 'M' or check_out_of_bounds(ws, i-(-1 if reverse else 1), j) is False:
            return False
        if ws[i-(-2 if reverse else 2)][j] != 'A' or check_out_of_bounds(ws, i-(-2 if reverse else 2), j) is False:
            return False
        if ws[i-(-3 if reverse else 3)][j] != 'S' or check_out_of_bounds(ws, i-(-3 if reverse else 3), j) is False:
            return False
        else:
            return True
    except IndexError:
        return False

#
# *--X
#

def sideways(ws: list[str], reverse: bool) -> bool:
    try:
        if ws[i][j-(-1 if reverse else 1)] != 'M' or check_out_of_bounds(ws, i, j-(-1 if reverse else 1)) is False:
            return False
        if ws[i][j-(-2 if reverse else 2)] != 'A' or check_out_of_bounds(ws, i, j-(-2 if reverse else 2)) is False:
            return False
        if ws[i][j-(-3 if reverse else 3)] != 'S' or check_out_of_bounds(ws, i, j-(-3 if reverse else 3)) is False:
            return False
        else:
            return True
    except IndexError:
        return False


for i in range(len(file)):
    for j in range(len(file[i])):
        if file[i][j] == 'X':
            if upwards(file, False):
                total += 1
                print(f'{total}: Up at [{i}, {j}]')
            if upwards(file, True):
                total += 1
                print(f'{total}: Down at [{i}, {j}]')
            if sideways(file, False):
                total += 1
                print(f'{total}: Left at [{i}, {j}]')
            if sideways(file, True):
                total += 1
                print(f'{total}: Right at [{i}, {j}]')
            if diag_left(file, False):
                total += 1
                print(f'{total}: Top Left at [{i}, {j}]')
            if diag_left(file, True):
                total += 1
                print(f'{total}: Bottom Right at [{i}, {j}]')
            if diag_right(file, False):
                total += 1
                print(f'{total}: Top Right at [{i}, {j}]')
            if diag_right(file, True):
                total += 1
                print(f'{total}: Bottom Left at [{i}, {j}]')

print(total)
