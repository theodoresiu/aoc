from collections import deque

def get_neighbors(x,y,lines):
    left = (x,y-1) if y > 0 else None
    right = (x,y+1) if y < len(lines[0])-1 else None
    top = (x-1,y) if x > 0 else None
    bot = (x+1,y) if x < len(lines)-1 else None
    return [i for i in [left, right,top,bot] if i]

def compare_steps(prev, new_step, lines):
    x1,y1 = prev
    x2,y2 = new_step
    if lines[x1][y1]=='S':
        return True
    new_step_letter = 'z' if lines[x2][y2]=='E' else lines[x2][y2]
    diff = ord(new_step_letter) - ord(lines[x1][y1])
    if diff==1 or diff==0 or diff < 0:
        return True
    return False

def compare_steps2(prev, new_step, lines):
    x1,y1 = prev
    x2,y2 = new_step
    old_step_letter = 'z' if lines[x1][y1]=='E' else lines[x1][y1]
    diff = ord(lines[x2][y2]) - ord(old_step_letter)
    if diff==-1 or diff==0 or diff > 0:
        return True
    return False


with open("../input.txt", 'r') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
#start =(20,0,0)
#end = (20,40)
#start =(0,0,0)
#end =(2,5)

#start =(20,0,0)
start = (20,40,0)

q =deque([start])
visited =set([start])
while q:
    x,y,count = q.popleft()
    #print(f"On the location: {(x,y,count)}")
    neighbors = get_neighbors(x,y,lines)
    for neigh in neighbors:
        if neigh not in visited and compare_steps2((x,y),neigh,lines):
            if lines[neigh[0]][neigh[1]]=="a":
                print(count+1)
                break
            else:
                q.append((neigh[0], neigh[1], count+1))
            visited.add(neigh)


