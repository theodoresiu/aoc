with open("../input.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip("\n") for line in lines]
colors_dict = {"red": 12,"blue": 14,"green": 13}
result = 0
result1 = 0
"""
for line in lines:
    l = line.split(":")
    game, rounds = l[0],l[1]
    good = True
    for round in rounds.split(";"):
        for colors in round.split(","):
            c = colors.strip().split(" ")
            count, color = c
            if int(count)>colors_dict[color]:
                good = False
                break
    if good:
        result+=int(game.lstrip("Game "))
print(result)

"""
result = 0
for line in lines:
    l = line.split(":")
    game, rounds = l[0],l[1]
    good = True
    min_dict ={}
    for round in rounds.split(";"):
        for colors in round.split(","):
            c = colors.strip().split(" ")
            count, color = c
            if color not in min_dict:
                min_dict[color]=int(count)
            elif int(count) > min_dict[color]:
                min_dict[color]=int(count)
    p=1
    print(min_dict)
    for _,val in min_dict.items():
        p=p*val
    result+=p
print(result)