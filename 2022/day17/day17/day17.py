with open("../input.txt", 'r') as f:
    pattern = list(f.readlines()[0])

rocks = [{"left":(0,0), "right":(3,0), "bottom":[(0,0),(1,0),(2,0),(3,0)], "rest":[]},
         {"left":(0,1), "right":(2,1), "bottom":[(0,1),(1,0),(2,1)], "rest":[(1,1),(1,2)]},
         {"left":(0,0), "right":(2,0), "bottom":[(0,0),(1,0),(2,0)], "rest":[(2,1),(2,2)]},
         {"left":(0,0), "right":(0,0), "bottom":[(0,0)], "rest":[(0,1),(0,2),(0,3)]},
         {"left":(0,0), "right":(1,0), "bottom":[(0,0),(1,0)], "rest":[(0,1),(1,1)]},
         ]

i=0
j=0
taken = set((0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6))
while j < 5:
    rock = rocks[j]
    btm = 0
    left, right = (rock['left'][0]+2, rock['left'][1]+btm+3), (rock['right'][0]+2, rock['left'][1]+btm+3)
    bottom =[(x[0]+2,x[1]+btm+3) for x in rock['bottom']]
    rest = [(x[0]+2,x[1]+btm+3) for x in rock['rest']]
    while True:
        if pattern[i]==">":
            if right[0]+1<7:
                #shift right
                right = (right[0]+1, right[1]-1)
                left = (left[0]+1, right[1]-1)
                bottom = [(bot[0]+1, bot[1]-1) for bot in bottom]
                rest = [(r[0]+1, r[1]-1) for r in rest]      
        elif pattern[i]=="<":
            if left[0]-1>=0:
                #shift left
                right = (right[0]-1, right[1]-1)
                left = (left[0]-1, left[1]-1)
                bottom = [(bot[0]+1, bot[1]-1) for bot in bottom]
                rest = [(r[0]+1, r[1]-1) for r in rest]
        found = False
        for bot in bottom:
            if (bot[0], bot[1]-1) in taken:
                found = True
                break
        if found:
            for bot in bottom:
                taken.add(bot)
            for r in rest:
                taken.add(r)
            btm = r[1]
            break
        i+=1
        if i == len(pattern):
            i=0
