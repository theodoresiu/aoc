def update_line(curr_line, location):
    if abs(len(curr_line)-location)<=1:
        curr_line+="#"
    else:
        curr_line+="."
    if len(curr_line)==40:
        print(curr_line)
        curr_line=""
    return curr_line

with open("../input.txt", 'r') as f:
    lines = f.readlines()


checkpoints = set([20,60,100,140,180,220])
location = 1
cycle = 1
result = 0
curr_line =""
for line in lines:
    cmds = line.strip().split(" ")
    curr_line = update_line(curr_line, location)
    if len(cmds)==2:
        curr_line = update_line(curr_line, location)
        location+= int(cmds[1])

    """
    if cycle+1 in checkpoints:
        #print(f"{cycle+1} at {score} for {(cycle+1)*score} in middle")
        result+=(cycle+1)*score
              
    else:
        cycle+=2
        score+= int(cmds[1])
        if cycle in checkpoints:
            #print(f"{cycle} at {score} for {(cycle)*score}")
            result+=(cycle)*score
    """


#print(result)