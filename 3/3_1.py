import re

with open("input_1.txt") as f:
    values = f.read().splitlines()


total = 0

for i in values:
    match = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', i)
    for j in match:
        total += int(j[0]) * int(j[1])

print(total)