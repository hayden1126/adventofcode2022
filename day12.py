map = open('day12.txt').read().strip().splitlines()
height, width = len(map), len(map[0])
print(height, width)

map = ['Sabqponm',
'abcryxxl',
'accszExk',
'acctuvwj',
'abdefghi']

for index, line in enumerate(map):
    if 'S' in line:
        start = (index, line.find('S'))
    if 'E' in line:
        end = (index, line.find('E'))

print(start, end)

shortest = 2500
current = start
paths = []

def find_next(previous, current, temp_path):
    next = [(previous[0]+1, previous[1]), (previous[0]-1, previous[1]), (previous[0], previous[1]+1), (previous[0], previous[1]-1)]
    if end in next:
        temp_path.append(end)
        length = len(temp_path)
        if length < shortest:
            shortest = length
            paths.append(temp_path)
        temp_path = temp_path[:-1]
        return
    temp_next = [n for n in next if n != current and (n[0] >= 0 and n[1] >= 0) and (n[0] < 5 and n[1] < 8)]
    try:
        temp_next = [n for n in temp_next if map[n[0]][n[1]] >= map[previous[0]][previous[1]]]
    except:
        print(temp_next, previous)
        exit()
    if len(temp_next) == 0:
        temp_path = temp_path[:-1]
        return
    for n in temp_next:
        temp_path.append(n)
        if len(temp_path) > 980:
            return
        find_next(current, n, temp_path)

temp_path = []
next = [(current[0]+1, current[1]), (current[0]-1, current[1]), (current[0], current[1]+1), (current[0], current[1]-1)]
temp_next = [n for n in next if (n[0] >= 0 and n[1] >= 0)]
for previous in temp_next:
    find_next(previous, current, temp_path)
print(paths)

path = []
shortest = 2000
current = start
def find_next():
    next = [(current[0]+1, current[1]), (current[0]-1, current[1]), (current[0], current[1]+1), (current[0], current[1]-1)]
    next = [n for n in next if n[0] < height and n[1] < width and n[0] > -1 and n[1] > -1 and map[current[0]][current[1]] >= map[n[0]][n[1]]]
    if end in next:
        
    for n in next:
        current = n
        find_next()