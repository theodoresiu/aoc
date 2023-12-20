from collections import defaultdict
from time import sleep

def buy_robot(ore,clay,obsidian):
    gem_stash['ore']-=ore
    gem_stash['clay']-=clay
    gem_stash['obsidian']-=obsidian

def return_robot(ore,clay,obsidian):
    gem_stash['ore']+=ore
    gem_stash['clay']+=clay
    gem_stash['obsidian']+=obsidian

def process_gems(time):
    print(f"time {time}, result {result}, robot {robots}, in {gem_stash}")
    sleep(.5)
    if time == 5:
        if gem_stash['geode']>result[0]:
            result[0]=gem_stash['geode']
            print(f"Top geode {result[0]}")
        return
    gems = (gem_stash['ore'],gem_stash['clay'],gem_stash['obsidian'])
    for val in vals:
        if all([(a >= b) for a, b in zip(gems,val['price'])]):
            buy_robot(gems[0], gems[1], gems[2])
            old_geode = gem_stash['geode']
            for robot,value in robots.items():
                gem_stash[robot]+=value
            robots[val['name']]+=1
            process_gems(time+1)
            ### huge back track
            robots[val['name']]-=1 # backtrack robot
            return_robot(gems[0], gems[1], gems[2]) # get money back
            for robot,value in robots.items(): #Remove what we farmed
                gem_stash[robot]-=value
            gem_stash['geode']=old_geode  
    for robot,val in robots.items():
        gem_stash[robot]+=val 
    process_gems(time+1)

    
            
result = [0]
vals = [{'name':'ore','price':(4,0,0)},
        {'name':'clay','price':(2,0,0)},
        {'name':'obsidian', 'price':(3,14,0)},
        {'name':'geode','price':(0,2,7)}]
robots = defaultdict(int)
gem_stash = defaultdict(int)
robots['ore']=1
process_gems(1)
