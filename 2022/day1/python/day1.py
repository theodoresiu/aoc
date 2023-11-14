import heapq

with open("../input.txt", "r+") as f:
    lines = f.readlines()

vals = []
max_score, curr_score, max_three = 0,0,0
for line in lines:
    if line=="\n":
        if curr_score > max_score:
            max_score = curr_score
        heapq.heappush(vals, -curr_score)
        curr_score =0
    else:
        curr_score+=int(line)

print(max_score)
for i in range(0,3):
    max_three+=-heapq.heappop(vals)
print(max_three)