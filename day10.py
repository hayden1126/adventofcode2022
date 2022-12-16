# Part 1
ls = open('day10.txt').read().strip().splitlines()

x = 1
cycles = [1] # index is how many cycles have past
cycle = 0
periods = [40, 80, 120, 160, 200, 240]

for l in ls:
    line = l.split()
    if line[0] == 'noop':
        cycles.append(x)
        cycle += 1
        if cycle in periods:
            print()
        if cycle%40 in [x-1, x, x+1]:
            print('#', end='')
        else:
            print(' ', end='')
        
    else:
        cycles.append(x)
        cycle += 1
        if cycle in periods:
            print()
        if cycle%40 in [x-1, x, x+1]:
            print('#', end='')
        else:
            print(' ', end='')
        x += int(line[1])
        cycles.append(x)
        cycle += 1
        if cycle in periods:
            print()
        if cycle%40 in [x-1, x, x+1]:
            print('#', end='')
        else:
            print(' ', end='')
        # print(x)

sum = 0
for n in [20, 60, 100, 140, 180, 220]:
    # print(cycles[n-1])
    sum += (n*cycles[n-1])
print(sum)
