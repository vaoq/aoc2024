with open("input_1.txt") as f:
    values = f.read().splitlines()
    values = [_.split() for _ in values]

total_safe = 0

for i in values:
    nums = []
    for j in range(len(i)-1):
        nums.append(int(i[j])-int(i[j+1]))
    if (False in [1 <= i <= 3 for i in nums]) and (False in [-1 >= i >= -3 for i in nums]):
        pass
    else:
        total_safe += 1

print(total_safe)