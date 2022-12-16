map = open('day12.txt').read().strip().splitlines()

for index, line in enumerate(map):
    if 'S' in line:
        start = (index, line.find('S'))

print(start)
