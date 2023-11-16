def process_parts(p1, p2):
    s1 = set()
    for c in p1:
        s1.add(c)
    for c in p2:
        if c in s1:
            return c
    return None

def process_three(x,y,z):
    x = set(x.strip())
    y = set(y.strip())
    z = set(z.strip())
    result = x.intersection(y).intersection(z).pop()
    return result

def calc_score(c):
    if c.lower()==c:
        return ord(c)-96
    return ord(c)-64+26

with open('../input.txt', 'r') as f:
    lines = f.readlines()

otherlines=lines.copy()
otherlines = [otherlines[i:i+3] for i in range(0,len(otherlines),3)]
print(otherlines[0])

s,t = 0,0
counter=0
for line in lines:
    line = line.strip("\n")
    p1, p2 = line[:len(line)//2], line[len(line)//2:]
    c = process_parts(p1,p2)
    s+= calc_score(c)

for three in otherlines:
    c = process_three(three[0],three[1],three[2])
    t+= calc_score(c)


print(s)
print(t)

