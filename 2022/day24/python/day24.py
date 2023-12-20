from collections import deque

def get_blizzards(lines):
    blizzards = set()
    for i in range(0,lines):
        for j in range(0, len(lines[0])):
            if lines[i][j]!=".":
                blizzards.add((lines[i][j],i,j))
    return blizzards

def update_blizzards(blizzards, lines):
    new_blizzard = set()
    blizz = set()
    for blizzard in blizzards:
        d,i,j = blizzard
        if d==">":
            if j+1<len(lines[0]):
                blizz.add((i,j+1))
                new_blizzard.add((d,i,j+1))
            else:
                blizz.add((i,0))
                new_blizzard.add((d,i,0))
        elif d=="<":
            if j-1>=0:
                blizz.add((i,j-1))
                new_blizzard.add((d,i,j-1))
            else:
                blizz.add((i,len(lines[0]))-1))
                new_blizzard.add((d,i,len(lines[0]))-1)
        elif d=="v":
            if i+1<len(lines):
                blizz.add((i+1,j))
                new_blizzard.add((d,i+1,j))
            else:
                blizz.add(i,0)
                new_blizzard.add((d,i,0))
        else:
            if i-1>=0:
                blizz.add((i-1,j))
                new_blizzard.add((d,i-1,j))
            else:
                blizz.add(len(lines)-1,0)
                new_blizzard.add((d,len(lines)-1,j))
    return new_blizzard,blizz

def get_directions(curr,lines):
    if curr==None:
        return [(0,0)]
    


with open("../input.txt", 'r') as f:
    lines = f.readlines()

lines=lines[1:]
lines=lines[:-1]
lines = [list(line.strip("\n"))[1:-1] for line in lines]
blizzards = get_blizzards(lines)
time = 0
curr=None
val = (time,curr,blizzards)
q = deque([val])
while True:
    time,curr,blizzards = q.popleft()
    if curr == (len(lines)-1, len(lines[0])-1):
        break
    blizzards,blizz = update_blizzards(blizzards,lines)
    for neigh in get_directions(curr):
        if neigh not in blizz:
            q.append(time+1, neigh, blizzards)
print(time+1)