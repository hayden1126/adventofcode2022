ls = []
print("input: ")
i = input()
while i != "exit":
    ls.append(i.split())
    i = input() 
# print(ls)

head = [0, 0]
tail = [0, 0]
tail_pos = set()

for move in ls:
    direction = move[0]
    steps = int(move[1])
    
