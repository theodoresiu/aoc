import re

with open("../input.txt", 'r') as f:
    lines = f.readlines()

maze = [list(line.strip("\n")) for line in lines]
print(len(maze[0]))
curr = (0,8)
direction = "right"
turns ={"right":{"R":"down","L":"up"},
        "left":{"R":"up","L":"down"},
        "up":{"R":"right","L":"left"},
        "down":{"R":"left","L":"right"}}
input = "10R5L5R10L4R5L5"
direction = [d for d in re.split(r'[\d*]',input) if d]
steps = re.split(r'[RL]',input)
for i in range(0,len(steps)):
    step_count = steps[i]
    for j in range(0,step_count):
        if direction=="right":
            if curr[1]+1 < len(maze[curr[0]])-1:
                next_step = (curr[0],curr[1]+1)
            else:
                s = maze[curr[0]].index(".")
                next_step = (curr[0],s)
        elif direction =="left":
            if curr[1]-1 >= 0:
                next_step = (curr[0],curr[1]-1)
            else:
                s = len(curr[0]) - maze[curr[0]][::-1].index(".")-1
                next_step = (curr[0],s)
        elif direction =="up":
            if curr[0]-1 < 0:
                next_step = (curr[0]-1,curr[1])
            else:
                for k in range(0,len(maze)):
                    if len(maze[k])>=curr[1]:
                        next_step = (k,curr[1])
                        break
        else:
            if curr[0]+1 < len(maze)-1:
                next_step = (curr[0]+1,curr[1])
            else:
                for k in range(len(maze)-1,-1,-1):
                    if len(maze[k])>=curr[1]:
                        next_step = (k,curr[1])
                        break

        if next_step ==".":
            curr = next_step
    direction = turns[direction][i]

print(curr)



