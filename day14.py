test_mode = True
if test_mode:
    height = 12
    width = 20
    filename = 'day14t.txt'
else:
    height = 150
    width = 100
    filename = 'day14.txt'
file = open(filename).read().strip().splitlines()
drop_point = (500-490, 1)

def setup(w, h):
    map = [['.' for _ in range(w)] for _ in range(h)]
    # note: convert x-axis to 1-100 from around 495-585
    for line in file:
        # print('line:', line)
        walls = line.split(' -> ')
        for i in range(len(walls)-1):
            horizontal = [int(walls[i].split(',')[0]), int(walls[i+1].split(',')[0])]
            vertical = [int(walls[i].split(',')[1]), int(walls[i+1].split(',')[1])]
            # print(horizontal)
            # print(vertical)
            for x in range(min(horizontal)-490, max(horizontal)+1-490):
                for y in range(min(vertical)-10, max(vertical)+1-10):
                    map[y][x] = '#'
            map[drop_point[1]-1][drop_point[0]] = '+'
    
    return map

def visualize(map):
    for row in map:
        for block in row:
            print(block, end='')
        print()

def fall():
    current_y, current_x = drop_point[1], drop_point[0]
    while True:
        # print(current_y, current_x)
        try:
            # Check directly below
            if map[current_y+1][current_x] == '.':
                # print(True)
                current_y += 1
            # Check diagonal left
            elif map[current_y+1][current_x-1] == '.':
                # print(0)
                current_y += 1
                current_x -= 1
            # Check diagonal right
            elif map[current_y+1][current_x+1] == '.':
                # print(0)
                current_x += 1
                current_y += 1
            # Else: stuck, fallen to bottom
            else:
                map[current_y][current_x] = 'o'
                return True
        except:
            # print(current_y, current_x)
            return False

# Part 1
map = setup(width, height)
times = 0
while fall():
    times += 1
print(times)
visualize(map)


# Part 2

# answers = [1, 2]
# n = 100

# while answers[0] != answers[1]:
#     answers.pop(0)
#     n += 1
#     print(n)
#     map = setup(width + n, height)
#     map[-1] = ['#' for _ in range(width + n)]
#     times = 0
#     while fall2() == True:
#         times += 1
#         if times%100000000 == 0:
#             print(times)
#             visualize(map)
#     answers.append(times)
#     print(answers)

# print(answers)

n = 0
map = setup(width, height)
map[-1] = ['#' for _ in range(width + n)]
times = 0
current_y, current_x = drop_point[1], drop_point[0]

while fall(current_y, current_x) == True:
    times += 1
if (current_y, current_x) == (drop_point[1], drop_point[0]):
    print('done')
if current_x
    
    # if times%100000000 == 0:
    #     print(times)
    #     visualize(map)

def expand(map):
    pass

def fall2(current_y, current_x):
    while True:
        # print(current_y, current_x)
        try:
            # Check directly below
            if map[current_y+1][current_x] == '.':
                # print(True)
                current_y += 1
            # Check diagonal left
            elif map[current_y+1][current_x-1] == '.':
                # print(0)
                current_y += 1
                current_x -= 1
            # Check diagonal right
            elif map[current_y+1][current_x+1] == '.':
                # print(0)
                current_x += 1
                current_y += 1
            # Else: stuck, fallen to bottom
            else:
                if map[current_y][current_x] == '+':
                    print('done')
                    return 'done' 
                map[current_y][current_x] = 'o'
                return True
            if current_x - 1 == 0 or current_x + 2 == width:
                expand(map)
                current_x += 1 # maybe add by the return value of expand(map) to shift the current_x along with the map
                n += 1
        except:
            # print(current_y, current_x)
            return False
