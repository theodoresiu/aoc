import ast
def in_order(p1, p2):
    i=0
    while i < len(p1):
        if i>=len(p2):
            return False
        val1, val2 = p1[i],p2[i]
        if isinstance(val1, int) and isinstance(val2, int):
            if val1>val2:
                return False
        else:
            if isinstance(val1,int):
                val1=[val1]
            else:
                val2=[val2]
            if not in_order(val1,val2):
                return False
        i+=1
    return True
            
with open("../input.txt", 'r') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
pairs = [ lines[i:i+3] for i in range(0,len(lines),3) ]
count=0
for pair in pairs:
    p1,p2 = ast.literal_eval(pair[0]), ast.literal_eval(pair[1])
    print(f"{p1} vs {p2}")
    if in_order(p1,p2):
        print("in-order")
        count+=1
print(count)

