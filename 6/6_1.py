with open("input_1.txt") as f:
    file = f.read().splitlines()

def find_player(puzzle: list[str]) -> list[int]:
    for i in range(len(puzzle)):
        result = [i]
        for j in ['v', '<', '>', '^']:
            index = puzzle[i].find(j)
            if index != -1:
                result.append(index)
                return result

def player_direction(puzzle: list[str], location: list[int]) -> str:
    player = puzzle[location[0]][location[1]]
    return player


def moving(puzzle: list[str]) -> list[str]:
    ahead = ''

    while ahead != '#':
        current = find_player(puzzle)
        direction = player_direction(puzzle, current)
        index = []
        if direction == '^':
            index.append(current[0]-1)
            index.append(current[1])
            ahead = puzzle[current[0]-1][current[1]]
        elif direction == '>':
            index.append(current[0])
            index.append(current[1]+1)
            ahead = puzzle[current[0]][current[1]+1]
        elif direction == '<':
            index.append(current[0])
            index.append(current[1]-1)
            ahead = puzzle[current[0]][current[1]-1]
        elif direction == 'v':
            index.append(current[0]+1)
            index.append(current[1])
            ahead = puzzle[current[0]+1][current[1]]

        if ahead != '#':
            puzzle[current[0]] = puzzle[current[0]][:current[1]] + 'X' + puzzle[current[0]][current[1]+1:]
            puzzle[index[0]] = puzzle[index[0]][:index[1]] + direction + puzzle[index[0]][index[1]+1:]
        else:
            puzzle = turn(puzzle, ahead)

        return puzzle


def turn(puzzle, next_cell) -> list[str]:
    player = find_player(puzzle)
    direction = player_direction(puzzle, player)
    if direction == '^':
        puzzle[player[0]] = puzzle[player[0]][:player[1]] + '>' + puzzle[player[0]][player[1]+1:]
    elif direction == '>':
        puzzle[player[0]] = puzzle[player[0]][:player[1]] + 'v' + puzzle[player[0]][player[1] + 1:]
    elif direction == '<':
        puzzle[player[0]] = puzzle[player[0]][:player[1]] + '^' + puzzle[player[0]][player[1] + 1:]
    elif direction == 'v':
        puzzle[player[0]] = puzzle[player[0]][:player[1]] + '<' + puzzle[player[0]][player[1] + 1:]
    return puzzle


while True:
    try:
        file = moving(file)
    except IndexError:
        print(sum([i.count('X') for i in file])+1)
        input()