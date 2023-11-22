def process_directory(lines):
    curr_sum = 0
    while lines:
        l = lines.pop(0).strip()
        cmds = l.split(" ")
        n1,n2 = cmds[0], cmds[1]
        if len(cmds)==3:
            n3 = cmds[2]

        if n1.isdigit():
            curr_sum+=int(n1)
        elif n2 == 'cd':
            if n3=="..":
                print(curr_sum)
                other_result.append(curr_sum)
                if curr_sum <= 100000:
                    result[0] +=curr_sum
                return curr_sum
            else:
                curr_sum += process_directory(lines)
    if curr_sum <= 10000:
        result[0]+= curr_sum
    return curr_sum
                        
result = [0]
other_result = []

with open("../input.txt", 'r') as f:
    lines = f.readlines()

c = process_directory(lines)
print(sorted(other_result))
print(c)

