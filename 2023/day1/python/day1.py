def process_lines(lines):
    result =0
    for line in lines:
        s=""
        rev = line[::-1]
        for i in line:
            if i.isdigit():
                s=i
                break
        for i in rev:
            if i.isdigit():
                s+=i
                break
        result+=int(s)
    return result
        
def process_lines2(lines):
    result =0
    lookup = {"o":[{"name":"one","val":"1"}],
     "t":[{"name":"two","val":"2"},
          {"name":"three","val":"3"}],
     "f":[{"name":"four","val":"4"},{"name":"five","val":"5"}],
     "s":[{"name":"six","val":"6"},{"name":"seven","val":"7"}],
     "e":[{"name":"eight","val":"8"}],
     "n":[{"name":"nine","val":"9"}],
     }
    for line in lines:
        val =None
        for i in range(0,len(line)):
            if line[i].isdigit():
                s=line[i]
                if not val:
                    val = s
            elif line[i] in lookup:
                for word in lookup[line[i]]:
                    name = word["name"]
                    if line[i:i+len(name)]==name:
                        s=word["val"]
                        if not val:
                            val = s
                        break
        #print((val,s))
        result+=int(val+s)
    return result

with open("../input.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip("\n") for line in lines]
#result = process_lines(lines)
r2 = process_lines2(lines)
print(r2)
#print(result)