from time import sleep
with open("../input.txt", 'r') as f:
    lines = f.readlines()

lines = [int(line.strip()) for line in lines]
i=0

while i < len(lines):
    print(i,lines[i],lines)
    if isinstance(lines[i],int):
        jump = lines[i]
        if jump>0:
            if i+jump < len(lines):
                lines = lines[:i]+lines[i+1:i+jump+1]+[(jump,0)]+lines[i+jump+1:]
            else:
                index = (i+jump)%len(lines)
                print(f"modded to {index}")
                lines = lines[:i]+lines[i+1:]
                print(lines)
                lines = lines[:index]+[(jump,0)]+lines[index:]
        elif jump<0:
            if i+jump>=0:
                lines = lines[:i]+lines[i+1:]
                lines = lines[:i+jump]+[(jump,0)]+lines[i+jump:]
            else:
                index = (i+jump)%len(lines)-2
                print(f"modded to {index}")
                lines = lines[:i]+lines[i+1:]
                print(lines)
                lines = lines[:index+1]+[(jump,0)]+lines[index+1:]
        else:
            lines = lines[:i]+[(jump,0)]+lines[i+1:]
    else:
        i+=1
print([line[0] for line in lines])