sign_score = {'Y':2,'Z':3,'X':1}
sign_trans = {'A':'X','B':'Y','C':'Z'}
opp_wins = {'A':'Z','B':'X','C':'Y'}
opp_loses = {'A':'Y','B':'Z','C':'X'}

with open("../input.txt", 'r') as f:
    lines = f.readlines()

curr_score1, curr_score2 = 0, 0
for line in lines:
    plays = line.rstrip('\n').split(" ")
    them, you = plays[0], plays[1]
    curr_score1 += sign_score[you]
    if sign_trans[them] == you:
        curr_score1+=3
    elif opp_wins[them] != you:
        curr_score1+=6

    if you == 'Y':
        curr_score2+=3
        curr_score2+=sign_score[sign_trans[them]]
    elif you =='X':
        curr_score2+=sign_score[opp_wins[them]]
    else:
        curr_score2+=6
        curr_score2+=sign_score[opp_loses[them]]

print(curr_score1)
print(curr_score2)