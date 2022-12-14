# Assuming map is square
map = []
print("input: ")
i = input()
while i != "exit":
    map.append([int(n) for n in i])
    i = input() 
# print(map)

side_length = len(map)

# Part 1
total = 0
total += 2*(2*side_length - 2)
for row_n, row in enumerate(map):
    for col_n, height in enumerate(row):
        if row_n in [0, side_length-1] or col_n in [0, side_length-1]:
            continue
        
        # If tree is not visible in the left/right direction
        if max(row[:col_n]) < height or max(row[col_n+1:]) < height or max([row2[col_n] for row2 in map][:row_n]) < height or max([row2[col_n] for row2 in map][row_n+1:]) < height:
                total += 1

print(total, side_length*side_length-total)

# Part 2 2283336
scores = []
for row_n, row in enumerate(map):
    for col_n, height in enumerate(row):
        left, right, up, down = 0, 0, 0, 0
        if row_n in [0, side_length-1] or col_n in [0, side_length-1]:
            continue
        
        # Left
        for h in row[:col_n][::-1]:
            left += 1
            if h >= height:
                break

        # Right
        for h in row[col_n+1:]:
            right += 1
            if h >= height:
                break
        
        # Up
        for h in [row2[col_n] for row2 in map][:row_n][::-1]:
            up += 1
            if h >= height:
                break
        
        # Down
        for h in [row2[col_n] for row2 in map][row_n+1:]:
            down += 1
            if h >= height:
                break
        scores.append(left*right*up*down)

print(max(scores))