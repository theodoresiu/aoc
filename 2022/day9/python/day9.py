def move_horizontal(head, tail, steps, direction,x):
    for i in range(0,int(steps)):
        new_head=(head[0]+direction,head[1])
        if head==tail or tail==new_head or abs(new_head[0]-tail[0])<2:
            new_tail=tail
        else:
            new_tail=new_head[0]-direction, new_head[1]
        head,tail = new_head, new_tail
        print(head,tail)
        x.append(tail)

    return head,tail

def move_vertical(head, tail, steps, direction,x):
    for i in range(0,int(steps)):
        new_head=(head[0],head[1]+direction)
        if head==tail or tail==new_head or abs(new_head[1]-tail[1])<2:
            new_tail=tail
        else:
            new_tail=new_head[0], new_head[1]-direction
        head,tail = new_head, new_tail
        print(head,tail)
        x.append(tail)

    return head,tail        

with open("../input.txt", 'r') as f:
    lines = f.readlines()


x = []
head,tail = (0,0),(0,0)
for line in lines:
    direction, step = line.strip().split(" ")
    if direction == "R":
        head, tail = move_horizontal(head, tail, step, 1, x)
    elif direction == "L":
        head, tail = move_horizontal(head, tail, step, -1, x)
    elif direction == "U":
        head, tail = move_vertical(head, tail, step, 1, x)
    else:
        head, tail = move_vertical(head, tail, step, -1, x)

x=x[:-10]
print(len(set(x)))
#print(x)
#print(len(x))