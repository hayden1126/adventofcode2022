file = open('day13.txt').read().strip().splitlines()
pairs = []
for i in range(0, len(file), 3):
    pairs.append([file[i], file[i+1]])
right_pairs = []

def compare(a, b):
    if type(a) == list or type(b) == list:
        if a == None and b != None:
            return 1
        if type(a) == int:
            a = [a]
        if type(b) == int:
            b = [b]
        length = [len(a), len(b)]
        if length[0] == 0 and length[1] > 0:
            return 1
        for i in range(min(length)):
            result = compare(a[i], b[i]) 
            if result == -1:
                return -1
            elif result == 1:
                return 1
            
        if length[0] > length[1]:
            return -1
        elif length[0] < length[1]:
            return 1
            
    else:
        if a < b:
            return 1
        elif a == b:
            return 0
        else:
            return -1


sum = 0
right_index = []
for index, pair in enumerate(pairs):
    a = eval(pair[0])
    b = eval(pair[1])
    res = compare(a, b)
    if res in [0, 1]:
        right_pairs.append(pair)
        sum += (index + 1)
        right_index.append(index+1)

print(sum)

# PART 2 -------------------------------------------------

# flatten: flattens list and gets length
def flatten(input_list):
    expand = input_list
    while True:
        complete = True
        for n in input_list:
            if type(n) == list:
                complete = False
                if len(n) > 0:
                    expand.extend(n)
                else:
                    expand.append(-1)
                expand.remove(n)
        if complete:
            break
    return len(expand)

def sort_special(ls):  
    ls.append([[2]])
    ls.append([[6]])
    try:
        return sorted(ls)
    except:
        sorted_special = {}
        for item in ls:
            start = item
            # Find the first value
            while type(start) == list:
                if len(start) > 0:
                    start = start[0]
                else:
                    start = '-1'
            flattened_list = [copy for copy in item]
            length = flatten(flattened_list)

            try:
                sorted_special[str(start)].append((item, length))
            except:
                sorted_special[str(start)] = [(item, length)]
            sorted_special[str(start)].sort(key=lambda x: x[1])
        return sorted_special

pairs_unorganized = []
for l in file:
    if l != '':
        pairs_unorganized.append(eval(l))

sorted_pairs = sort_special(pairs_unorganized)
index = 0
key1, key2 = 0, 0
combined_list = []
for item, value in sorted_pairs.items():
    combined_list.append([item, value])
    
combined_list.sort(key=lambda x:int((x[0])))

for a in combined_list:
    for b in a[1]:
        index += 1
        if b[0] == [[2]]:
            key1 = index
        if b[0] == [[6]]:
            key2 = index

print(key1*key2)

