from collections import defaultdict

def process_part(val):
    val = val.split(",")
    x = int(val[0].split("=")[1])
    y = int(val[1].split("=")[1])
    return [x,y]


def process_lines(lines):
    result = []
    for line in lines:
        sensor,beacon = line.split(":")
        sensor = sensor.lstrip("Sensor at ")
        beacon = beacon.lstrip(" closest beacon is at ")
        result.append(process_part(sensor)+process_part(beacon))
    return result
         




with open("../input.txt", 'r') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

processed_lines = process_lines(lines)
result = defaultdict(set)
print(processed_lines)
for line in processed_lines:
    s_x,s_y,b_x,b_y = line
    diff = abs(s_x-b_x)+abs(s_y-b_y)
    #print(diff)
    for i in range(s_y,s_y+diff+1):
        remaining = s_y+diff-i
        for j in range(s_x-remaining,s_x+remaining+1):
            if i!=s_x and j!=s_y:
                result[i].add(j)
    for i in range(s_y,s_y-diff-1,-1):
        remaining = i-(s_y-diff)
        for j in range(s_x-remaining,s_x+remaining+1):
            if i!=s_x and j!=s_y:
                result[i].add(j)
print(len(result[10]))


