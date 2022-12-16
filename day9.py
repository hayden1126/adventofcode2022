ls = open('day9.txt').read().strip().splitlines()

knots = 10 # = 2 if Part 1
direction = {'L': [-1, 0], 'R': [1, 0], 'U': [0, 1], 'D': [0, -1]}

coords = [[0, 0] for _ in range(knots)]
tail_pos = set()
for move in ls:
    dir, steps = move.split()
    # For each repeated step
    for _ in range(int(steps)):
        coords[0][0] += direction[dir][0]
        coords[0][1] += direction[dir][1]
        for index in range(knots-1):
            x_diff, y_diff = coords[index][0] - coords[index+1][0], coords[index][1] - coords[index+1][1]
            if abs(x_diff)!=2 and abs(y_diff)!=2:
                continue
            # If knot has to move
            if x_diff:
                x_diff = int(x_diff / abs(x_diff))
            if y_diff:
                y_diff = int(y_diff / abs(y_diff))        
            coords[index+1][0] += x_diff
            coords[index+1][1] += y_diff
        tail_pos.add(f"{str(coords[knots-1][0])},{str(coords[knots-1][1])}")
print(len(tail_pos))