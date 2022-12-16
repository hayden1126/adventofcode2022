# items = [[85, 79, 63, 72], [53, 94, 65, 81, 93, 73, 57, 92], [62, 63], [57, 92, 56], [67], [85, 56, 66, 72, 57, 99], [86, 65, 98, 97, 69], [87, 68, 92, 66, 91, 50, 68]]
from sympy.ntheory import factorint

monkeys = [
    {
        'items': [85, 79, 63, 72], 
        'operation': '*17', 
        'test': 2, 
        'true': 2, 
        'false': 6,
        'count': 0
    },
    {
        'items': [53, 94, 65, 81, 93, 73, 57, 92], 
        'operation': '**2', 
        'test': 7, 
        'true': 0, 
        'false': 2,
        'count': 0
    },
    {
        'items': [62, 63], 
        'operation': '+7', 
        'test': 13, 
        'true': 7, 
        'false': 6,
        'count': 0
    },
    {
        'items': [57, 92, 56], 
        'operation': '+4', 
        'test': 5, 
        'true': 4, 
        'false': 5,
        'count': 0
    },
    {
        'items': [67], 
        'operation': '+5', 
        'test': 3, 
        'true': 1, 
        'false': 5,
        'count': 0
    },
    {
        'items': [85, 56, 66, 72, 57, 99], 
        'operation': '+6', 
        'test': 19, 
        'true': 1, 
        'false': 0,
        'count': 0
    },
    {
        'items': [86, 65, 98, 97, 69], 
        'operation': '*13', 
        'test': 11, 
        'true': 3, 
        'false': 7,
        'count': 0
    },
    {
        'items': [87, 68, 92, 66, 91, 50, 68], 
        'operation': '+2', 
        'test': 17, 
        'true': 4, 
        'false': 3,
        'count': 0
    }
]

monkeys = [
    {
        'items': [79, 98], 
        'operation': '*19', 
        'test': 23, 
        'true': 2, 
        'false': 3,
        'count': 0
    },
    {
        'items': [54, 65, 75, 74], 
        'operation': '+6', 
        'test': 19, 
        'true': 2, 
        'false': 0,
        'count': 0
    },
    {
        'items': [79, 60, 97], 
        'operation': '**2', 
        'test': 13, 
        'true': 1, 
        'false': 3,
        'count': 0
    },
    {
        'items': [74], 
        'operation': '+3', 
        'test': 17, 
        'true': 0, 
        'false': 1,
        'count': 0
    }
]

rounds = 300
monkey_num = len(monkeys)
for _ in range(rounds):
    for i in range(monkey_num):
        monkey = monkeys[i]
        to_be_removed = []
        for index, item in enumerate(monkey['items']):
            monkey['count'] += 1
            new = eval(f"{int(item)}{monkey['operation']}")//3
            if new % monkey['test'] == 0:
                monkeys[monkey['true']]['items'].append(new)
            else:
                monkeys[monkey['false']]['items'].append(new)
            to_be_removed.append(index)
        for n in sorted(to_be_removed, reverse=True):
            monkey['items'].pop(n)

counts = [monkey['count'] for monkey in monkeys]
print(counts)
print(sorted(counts)[-1] * sorted(counts)[-2])