def get_neighbors(cube):
    x,y,z = cube
    left,right  = (x-1,y,z),(x+1,y,z)
    up,down = (x,y,z+1),(x,y,z-1)
    in_page,out_page = (x,y+1,z),(x,y-1,z)
    total =6
    for neigh in [left, right, up, down, in_page, out_page]:
        if neigh in cubes:
            total-=1
    visited.add(cube)
    result[0]=result[0]+total


with open("../input.txt", 'r') as f:
    cubes = f.readlines()

result = [0]
visited = set()
cubes = [tuple(cube.strip().split(",")) for cube in cubes]
cubes  = [(int(cube[0]),int(cube[1]),int(cube[2])) for cube in cubes]
for cube in cubes:
    get_neighbors(cube)

print(result)


