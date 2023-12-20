def get_elves(lines):
    elves = set()
    for i in range(0,len(lines)):
        for j in range(0,len(lines[0])):
            if lines[i][j]=="#":
                elves.add((i,j))

    return elves

def get_proposed_moves(elves,lines):
    proposed = {}
    for elf in elves:
        x,y = elf
        placed=False
        if x-1>=0:
            if lines[x-1][y]=="." and lines[x-1][y-1]=="." and lines[x-1][y+1]==".":
                placed = True
                if (x-1,y) in proposed:
                    proposed[(x-1,y)].append((x,y))
                    proposed[(x,y)]=[]
                else:
                    proposed[(x-1,y)]=[(x,y)]
        elif x+1<len(lines) and not placed:
            placed = True
            if lines[x+1][y]=="." and lines[x+1][y-1]=="." and lines[x+1][y+1]==".":
                if (x+1,y) in proposed:
                    proposed[(x+1,y)].append((x,y))
                    proposed[(x,y)]=[]
                else:
                    proposed[(x+1,y)]=[(x,y)]
        elif y-1>=0 and not placed:
            placed = True
            if lines[x][y-1]=="." and lines[x+1][y-1]=="." and lines[x-1][y-1]==".":
                if (x,y-1) in proposed:
                    proposed[(x,y-1)].append((x,y))
                    proposed[(x,y)]=[]
                else:
                    proposed[(x,y-1)]=[(x,y)]
        elif y+1<len(lines[0]) and not placed:
            placed = True
            if lines[x][y+1]=="." and lines[x+1][y+1]=="." and lines[x-1][y+1]==".":
                if (x,y-1) in proposed:
                    proposed[(x,y-1)].append((x,y))
                    proposed[(x,y)]=[]
                else:
                    proposed[(x,y-1)]=[(x,y)]

    for key,val in proposed.items():
        if len(val)>1:
            del proposed[key]
    return proposed


with open("../input.txt", 'r') as f:
    lines = f.readlines()

lines = [list(line.strip("\n")) for line in lines]
elves = get_elves(lines)

while True:
    no_moves = False
    proposed = get_proposed_moves(elves,lines)
    if not proposed:
        break
    elves = set(proposed.keys())
    lines = [['.' for i in range(0,len(lines[0]))] for j in range(0,len(lines))]
    for elf in elves:
        x,y = elf
        lines[x][y]="#"


