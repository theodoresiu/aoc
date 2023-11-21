import copy

containers = {}
containers[1]=["N","W", "F","R","Z","S","M","D"][::-1]
containers[2]=["S","G","Q","P","W"][::-1]
containers[3]=["C","J","N","F","Q","V","R","W"][::-1]
containers[4]=["L","D","G","C","P","Z","F"][::-1]
containers[5]=["S","P","T"][::-1]
containers[6]=["L","R","W","F","D","H"][::-1]
containers[7]=["C","D","N","Z"][::-1]
containers[8]=["Q","J","S","V","F","R","N","W"][::-1]
containers[9]=["V","W","Z","G","S","M","R"][::-1]

other_containers = copy.deepcopy(containers)

def process_move(initial, dest, crates):
    print((initial, dest, crates))
    i = containers[initial].copy()
    j = containers[dest].copy()

    move = i[len(i)-crates:]
    j = j+move[::-1]
    i = i[:len(i)-crates]
    containers[initial]=i
    containers[dest]=j

def process_other_move(initial, dest, crates):
    #print((initial, dest, crates))
    i = other_containers[initial].copy()
    j = other_containers[dest].copy()

    move = i[len(i)-crates:]
    j = j+move
    i = i[:len(i)-crates]
    other_containers[initial]=i
    other_containers[dest]=j
    

with open("../input.txt", 'r') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    if line.startswith("move"):
        print(line)
        _,crates,_,initial,_,dest = line.split(" ")
        process_move(int(initial), int(dest), int(crates))
        process_other_move(int(initial), int(dest), int(crates))

result = ""
other_result = ""
for i in range(1,10):
    result+=containers[i][-1]
    other_result+=other_containers[i][-1]
print(result)
print(other_result)
