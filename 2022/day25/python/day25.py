conversion = {"2":2,"1":1,"0":0,"-":-1,"=":-2}

def process_line(line):
    val = 0
    for i in range(0,len(line)):
        val+=conversion[line[i]]*5**i
    return val

def decimal_to_snafu(decimal):
    convert = {
    4: '-',
    3: '=',
    2: '2',
    1: '1',
    0: '0'}

    result = ""
    while decimal:
        remain = decimal % 5
        decimal = round(decimal/5)
        result+=convert[remain]
    return result[::-1]



with open("../input.txt", 'r') as f:
    lines = f.readlines()

result =0
lines = [line.strip("\n") for line in lines]
for line in lines:
    result+= process_line(line[::-1])
print(result)
print(decimal_to_snafu(result))
