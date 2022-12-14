# import json
'''
Assumptions:
1: No empty directories
2: "ls" will not run two times in a row
'''

inputs = []
print("input: ")
i = input()
while i != "exit":
    if i.startswith("$ ls"):
        temp = [i]
        j = input()
        while j != "exit" and not j.startswith("$"): # Assumption 1
            temp.append(j)
            j = input()
        inputs.append(temp)
        if j == "exit":
            break
        else:
            inputs.append(j) # Assumption 2
            i = input()
    else:
        inputs.append(i)
        i = input()
print(inputs)

# inputs = ['$ cd /', ['$ ls', 'dir a', '14848514 b.txt', '8504156 c.dat', 'dir d'], '$ cd a', ['$ ls', 'dir e', '29116 f', '2557 g', '62596 h.lst'], '$ cd e', ['$ ls', '584 i'], '$ cd ..', '$ cd ..', '$ cd d', ['$ ls', '4060174 j', '8033020 d.log', '5626152 d.ext', '7214296 k']]

directories = {}
temp_directory = directories
path = ["/"]
directory_sizes = {"/": [0]}

# STEP 1: Mapping out
for line in inputs[1:]:
    
    # If command is "ls"
    if type(line) == list:
        for item in line[1:]:
            temp = item.split()
            
            p = "-".join(path)
            # If directory
            if temp[0] == "dir":
                temp_directory[f"{p}-{temp[1]}"] = {}
                directory_sizes[f"{p}-{temp[1]}"] = [0]
                # print(path[-1])
                directory_sizes[p].append(f"{p}-{temp[1]}")
            # If file
            if temp[0].isnumeric():
                temp_directory[f"{p}-{temp[1]}"] = int(temp[0])
                directory_sizes[p][0] += int(temp[0])

    # If command is "cd"
    else: # type(line) == str:
        cd_path = line.split()[2]
        if cd_path == "..":
            path.pop(-1)
            temp_directory = directories
            for i in range(2, len(path)+1):
                temp_directory = temp_directory[f"{'-'.join(path[:i])}"]
        else:
            path.append(cd_path)
            temp_directory = temp_directory[f"{'-'.join(path)}"]
print(directories)
# print(directory_sizes)

#Step 2: Getting sizes for each directory
while True:
    complete = True
    # For each directory
    for directory, sizes in directory_sizes.items(): 
        # If directory is complete
        try:
            directory_sizes[directory] = [sum(sizes)]
        # If incomplete
        except:
            complete = False
            # For every included directory
            for index, size in enumerate(sizes): 
                if type(size) == str:
                    directory_sizes[directory].pop(index)
                    directory_sizes[directory] += directory_sizes[size]
    if complete:
        break
print(directory_sizes)

# Step 3: Get sum of all sizes of at most 100000
sum = 0
for directory, size in directory_sizes.items():
    if size[0] <= 100000:
        sum += size[0]
print(sum)

# Part 2
unused_space = 70000000 - directory_sizes['/'][0]
extra_space_needed = 30000000 - unused_space

smallest = directory_sizes['/'][0]
for directory, size in directory_sizes.items():
    if size[0] - extra_space_needed >= 0:
        if size[0] < smallest:
            smallest = size[0]

print(smallest)


'''
directories = 
{
'a': {
    'e': {
        'i': 584
        }, 
    'f': 29116, 
    'g': 2557, 
    'h.lst': 62596
    }, 
'b.txt': 14848514, 
'c.dat': 8504156, 
'd': {
    'j': 4060174, 
    'd.log': 8033020, 
    'd.ext': 5626152, 
    'k': 7214296
    }
}
'''

'''
To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)
Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
'''

# json_object = json.dumps(directories, indent = 4) 
# print(json_object)