with open("../input.txt", 'r') as f:
    lines = f.readlines()


checkpoints = set([20,60,100,140,180,220])
score = 1
cycle = 1
result = 0
for line in lines:
    cmds = line.strip().split(" ")
    if cycle+1 in checkpoints:
        #print(f"{cycle+1} at {score} for {(cycle+1)*score} in middle")
        result+=(cycle+1)*score
    if len(cmds)==1:
        cycle+=1          
    else:
        cycle+=2
        score+= int(cmds[1])
        if cycle in checkpoints:
            #print(f"{cycle} at {score} for {(cycle)*score}")
            result+=(cycle)*score

print(result)