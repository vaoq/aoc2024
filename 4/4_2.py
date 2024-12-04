with open("input_2.txt") as f:
    file = f.read().splitlines()

total = 0
matches = ["MMSS", "SMMS", "SSMM", "MSSM"]


def get_diagonals(ws: list[str]) -> bool:
    if (-1 >= i-1 or i-1 >= len(ws)) or (-1 >= j-1 or j-1 >= len(ws[i])):
        return False
    elif (-1 >= i-1 or i-1 >= len(ws)) or (-1 >= j+1 or j+1 >= len(ws[i])):
        return False
    elif (-1 >= i+1 or i+1 >= len(ws)) or (-1 >= j-1 or j-1 >= len(ws[i])):
        return False
    elif (-1 >= i+1 or i+1 >= len(ws)) or (-1 >= j+1 or j+1 >= len(ws[i])):
        return False
    else:
        return True if f"{ws[i-1][j-1]}{ws[i-1][j+1]}{ws[i+1][j+1]}{ws[i+1][j-1]}" in matches else False

for i in range(len(file)):
    for j in range(len(file[i])):
        if file[i][j] == 'A':
            if get_diagonals(file):
                total += 1

print(total)
