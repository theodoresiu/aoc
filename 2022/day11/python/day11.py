from math import floor

def process_monkey(monkey, monkey_stats):
    monkey_num = int(monkey[0].rstrip(":\n").lstrip("Monkey "))
    monkey_items = monkey[1].rstrip("\n").lstrip("  Starting items: ").split(",")
    monkey_operation = monkey[2].rstrip().lstrip("  Operation: new = ")
    monkey_test = monkey[3].rstrip("\n").lstrip("  Test: divisible by ")
    monkey_true = monkey[4].rstrip("\n").lstrip("    If true: throw to monkey ")
    monkey_false = monkey[5].rstrip("\n").lstrip("    If false: throw to monkey ")
    monkey_stats[monkey_num]={"items":[int(i) for i in monkey_items],
                              "operation": f"o{monkey_operation}",
                              "test":(int(monkey_test),int(monkey_true), int(monkey_false)), "count":0}
    
def monkey_toss(monkey_stats):
    for i in range(0,len(monkey_stats)):
        #print(f"On monkey {i}")
        for item in monkey_stats[i]['items']:
            monkey_stats[i]['count']+=1
            result = eval(monkey_stats[i]["operation"], {"old": item})
            #result = floor(result/3)
            #print((monkey_stats[i]["operation"], item, result))
            t,ift,iff = monkey_stats[i]["test"]
            if result % t ==0:
                #print(f"Thrown to {ift}")
                monkey_stats[ift]["items"].append(result)
            else:
                #print(f"Thrown to {iff}")
                monkey_stats[iff]["items"].append(result)
        monkey_stats[i]['items']=[]

with open("../input.txt", 'r') as f:
    lines = f.readlines()

monkeys = [ lines[i:i+7] for i in range(0,len(lines),7) ]
monkey_stats = {}
for monkey in monkeys:
    process_monkey(monkey, monkey_stats)
#print(monkey_stats)

for round in range(0,20):
    if round % 100 ==0:
        print(round)
        print(monkey_stats)
    monkey_toss(monkey_stats)
    #print(monkey_stats)

print(monkey_stats)
l = [monkey_stats[i]["count"] for i in monkey_stats.keys()]
print(sorted(l))