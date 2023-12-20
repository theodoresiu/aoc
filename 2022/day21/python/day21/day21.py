with open("../input.txt", 'r') as f:
    lines = f.readlines()

lines = [int(line.strip()) for line in lines]
result = {}
for line in lines:
    l = line.split(":")[0]
    key, value = l[0],l[1]
    if value.strip().isdigit():
        result[key]=int(value)
    else:
        if len(value.split("+"))==2:
            operation = "+"
            x = [int(num.strip()) for num in len(value.split("+"))]
        elif len(value.split("-"))==2:
            operation = "-"
            x = [int(num.strip()) for num in len(value.split("+"))]
        elif len(value.split("*"))==2:
            operation = "*"
            x = [int(num.strip()) for num in len(value.split("+"))]
        else:
            operation = "/"
            x = [int(num.strip()) for num in len(value.split("+"))]
        for i in range(0,2):
            if x[i] in result:
                x[i]=result[x[i]]
        result[key]={"nums":x, "operation":operation}

        
while True:
    found = False
    for k,v in result.items():
        if isinstance(v,list):
            for i in range(0,2):
                if isinstance(v['nums'][i],str) and isinstance(result[v['nums'][i]],int):
                    v['nums'][i]=result[v['nums'][i]]
            if isinstance(v['nums'][0],int) and isinstance(v['nums'][1],int):
                if v['operation']=="+":
                    result[k]=v['nums'][0]+v['nums'][1]
                elif v['operation']=="-":
                    result[k]=v['nums'][0]-v['nums'][1]
                elif v['operation']=="*":
                    result[k]=v['nums'][0]*v['nums'][1]
                else:
                    result[k]=v['nums'][0]/v['nums'][1]
                if k=='root' and isinstance(result[k],int):
                    found=True
                    break
    if found:
        break

print(result['root'])