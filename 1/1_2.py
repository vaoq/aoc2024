with open("input_1.txt") as f:
   values = f.read().splitlines()
   values = [_.split() for _ in values]

column_0 = [i[0] for i in values]
column_1 = [i[1] for i in values]

print(sum([(int(i) * column_1.count(i)) for i in column_0]))



