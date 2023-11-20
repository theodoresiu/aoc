

def get_range(r):
    result = r.split("-")
    i,j = int(result[0]), int(result[1])
    return i,j


with open('../input.txt', 'r') as f:
    lines = f.readlines()

s1,s2 = 0,0

for line in lines:
    line=line.strip()
    r1,r2=line.split(",")
    x1,x2= get_range(r1)
    y1,y2= get_range(r2)

    if (x1<=y1 and x2>=y2) or (y1<=x1 and y2>=x2):
        s1+=1

    if (x1<=y1 and x2>=y1) or (y1<=x1 and y2>=x1):
        s2+=1

print(s1)
print(s2)