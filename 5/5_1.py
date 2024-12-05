with open("input_1.txt") as f:
    f = f.read().split('\n\n')
    page_rules = [[int(j) for j in i] for i in [i.split('|') for i in f[0].split('\n')]]
    page_updates = [[int(j) for j in i] for i in [i.split(',') for i in f[1].split('\n')]]


def values_to_check(values: list[int], dictionary: dict[int: int]) -> dict[int: int]:
    temp_dict = {}
    for k, v in dictionary.items():
        if k in values:
            temp_dict.update({k:v})
    return temp_dict

rules: dict[int: list[int]] = {}
for i in page_rules:
    if i[0] in rules:
        rules[i[0]] += [i[1]]
    else:
        rules.update({i[0]:[i[1]]})



for each in page_updates:
    temp_rules = values_to_check(each, rules)
    printed_numbers = []
    print('----------------------------------------')
    for i in each:
        for k, v in temp_rules.items():
            if k not in printed_numbers:
                if (i in v):
                    print(f'{i} in [{k}: {v}]')
                else:
                    printed_numbers.append(i)
                    print(i)
                    break

# sort out checking when number has already been printed? WERE CLOSE