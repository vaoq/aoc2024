import re

with open("input_1.txt") as f:
    values = f.read().splitlines()

status = True
total = []
matches = [re.findall(r'(do\(\))|(don\'t\(\))|mul\((\d{1,3}),(\d{1,3})\)', values[i])for i in range(len(values))]

for match in matches:
    for i in match:
        if i[0]:
            status = True
        elif i[1]:
            status = False
        else:
            total.append(int(i[2]) * int(i[3])) if status else ()

print(sum(total))
