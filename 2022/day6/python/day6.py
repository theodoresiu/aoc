from collections import deque

with open("../input.txt", 'r') as f:
    line = f.readlines()[0]

line = line.strip()
q = deque(line[:14])
for index, char in enumerate(line[14:]):
    if len(set(q))==14:
        print(index+14)
        break
    else:
        q.popleft()
        q.append(char)
