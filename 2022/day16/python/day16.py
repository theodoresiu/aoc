from collections import defaultdict
from time import sleep

def process_lines(lines):
    for line in lines:
        pressure, tunnel = line.split(";")
        p = pressure.split("=")[1]
        valve = pressure.split(" has")[0].lstrip("Valve ")
        connections = tunnel.lstrip(" tunnels lead to valves ").split(",")
        for conn in connections:
            tunnels[valve].add(conn.strip())
        pressures[valve]={"p":int(p),"open":False}

def get_open(values):
    r =0 
    for value in values:
        if value['open']:
            r+=value["p"]
    return r

def iterate_through(valve, time, pressure,my_path):
    #print((valve,time,pressure))
    #print(f"My current path leading up {my_path}")
    #if my_path[:3]==['AA', 'DD+', 'CC',]:
    #    print((valve,time,pressure))
    #    print(f"My current path leading up {my_path}")

    if time==30:
        if pressure>=result[0]:
            print(my_path+[valve])
            print(f"Setting here at {pressure}")
            result[0]=pressure
        return
    #print(f"I can go to {tunnels[valve]}")
    for conns in tunnels[valve]:
        #Valve is open already just skip it
        if pressures[valve]["open"]:
            new_p = get_open(pressures.values())
            iterate_through(conns,time+1,pressure+new_p,my_path+[valve])
        else:
            #valve is closed consider opening it
            if time+2<=30:
                old_p = get_open(pressures.values())
                pressures[valve]["open"]=True
                new_p = get_open(pressures.values())
                iterate_through(conns,time+2,pressure+old_p+new_p,my_path+[f"{valve}+"])
                pressures[valve]["open"]=False #backtrack
            new_p = get_open(pressures.values())
            iterate_through(conns,time+1,pressure+new_p,my_path+[valve])
        #Open the valve
            

result= [0]

with open("../input.txt", 'r') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
pressures = {}
tunnels=defaultdict(set)
process_lines(lines)
print(pressures)
print(tunnels)
my_path = []
whats_open = set()
iterate_through("AA",0,0, my_path)
print(result[0])

