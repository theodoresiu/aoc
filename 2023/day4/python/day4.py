def check_sets(l):
    sets = l.split("|")
    set1 = set([int(i) for i in sets[0].split()])
    set2 = set([int(i) for i in sets[1].split()])
    #print(f"s1 {set1}, s2 {set2}, int {set1.intersection(set2)}")
    power = len(set1.intersection(set2))
    if power>=1:
        #print(2**(power-1))
        return 2**(power-1)
    return 0

with open("../input.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip("\n") for line in lines]
result = 0
for line in lines:
    l = line.split(":")[1].strip()
    result += check_sets(l)

print(result)
