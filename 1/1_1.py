with open("input_1.txt") as f:
    values = f.readlines()

for i in range(len(values)):
    values[i] = values[i].replace('\n', '').split()

column_0 = []
column_1 = []

for i in range(len(values)):
    column_0.append(values[i][0])
    column_1.append(values[i][1])

column_0 = sorted(column_0)
column_1 = sorted(column_1)

results = [abs(int(i[0])-int(i[1])) for i in zip(column_0, column_1)]

print(sum(results))
