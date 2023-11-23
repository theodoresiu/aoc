def get_tree_score(row, col, graph):
    max_score = 1
    curr = 0
    for i in range(col+1,len(graph[0])):
        if graph[row][col]>graph[row][i]:
            curr+=1
        else:
            curr+=1
            break
    #print(f"right: {curr}")
    max_score*=curr
    curr =0
    for i in range(col-1,-1,-1):
        if graph[row][col]>graph[row][i]:
            curr+=1
        else:
            curr+=1
            break
    #print(f"left: {curr}")
    max_score*=curr
    curr=0
    for i in range(row+1,len(graph)):
        if graph[row][col]>graph[i][col]:
            curr+=1
        else:
            curr+=1
            break
    max_score*=curr
    curr=0
    for i in range(row-1,-1,-1):
        if graph[row][col]>graph[i][col]:
            curr+=1
        else:
            curr+=1
            break
    max_score*=curr
    print(f"{(row,col)} index has score {max_score}")
    if result2[0]<max_score:
        result2[0]=max_score



with open("../input.txt", 'r') as f:
    lines = f.readlines()

result = []
for line in lines:
    result.append([int(x) for x in list(line.strip())])

"""
y = set()

for row in range(0,len(result)):
    prev = -1
    for col in range(0,len(result[row])):
        if result[row][col]>prev:
            y.add((row,col))
            prev = result[row][col]
    prev = -1
    for col in range(len(result)-1,-1,-1):
        if result[row][col]>prev:
            y.add((row,col))
            prev = result[row][col]

for col in range(0,len(result[0])):
    prev = -1
    for row in range(0,len(result)):
        if result[row][col]>prev:
            y.add((row,col))
            prev = result[row][col]
    prev = -1
    for row in range(len(result)-1,-1,-1):
        if result[row][col]>prev:
            y.add((row,col))
            prev = result[row][col]

print(len(y))
"""
result2 = [0]
for row in range(0,len(result)):
    for col in range(0, len(result[0])):
        get_tree_score(row, col, result)
print(result2)