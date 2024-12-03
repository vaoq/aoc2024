# i hate it here.

with open("input_2.txt") as f:
    file = f.read().splitlines()
    file = [_.split() for _ in file]

total = 0
full_safe_list = []
temp_safe_list = []


def list_str_to_list_int(arr: list[str]) -> list[int]:
    return [int(i) for i in arr]


def compare(arr: list[str]) -> list[bool]:
    arr = list_str_to_list_int(arr)
    result = []
    state = 'N'
    for i in range(len(arr)-1):
        difference = arr[i] - arr[i+1]
        if 1 <= difference <= 3 and (state == 'A' or state == 'N'):
            result.append(True)
            state = 'A'
        elif -1 >= difference >= -3 and (state == 'D' or state == 'N'):
            result.append(True)
            state = 'D'
        else:
            result.append(False)
    return result


for line in file:
    for i in range(len(line)):
        temp_line = line.copy()
        temp_line.pop(i)
        temp_safe_list.append(compare(temp_line))
    full_safe_list.append(temp_safe_list)
    temp_safe_list = []

for i in full_safe_list:
    safe = False
    for j in i:
        if j.count(True) == len(j):
            safe = True
            break
        else:
            safe = False
    if safe:
        total += 1

print(total)