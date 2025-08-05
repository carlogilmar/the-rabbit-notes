# Problem
## Given:
#bombs =
#[
#    [0,0,3], #b1 detonate
#    [2,1,2], #b2 detonate
#    [4,1,3], #detonate
#    [9,3,2]
#]
#
#b1 x1=0 y1=0
#b2 x2=2 y2=1
#0-2 + 0-1 = 3 <+ 3 -> detonate
#
#bombs= [
#    [7,5,5], # initial detonation
#    [3,3,1], # nope
#    [10,10,3] # nope
#]
#
#7-3 + 5-3 = 6
#
#bombs = [
#    [0,0,99], #intial detonate
#    [1,0,1], # detonate
#    [2,0,1],# detonate
#    [3,0,1] #detonate
#    [4,0,1] #detonate
#]

def detonation(bombs):
    for bomb in bombs:
    if len(bombs) == 2:
        [x1,y1,r1] = bombs[0]
        [x2,y2,r2] = bombs[1]
        distance = abs(x1-x2) + abs(y1-y2)
        if distance >= r1:
            return 1 # Detonation
        else:
            return 0 # Bomb not in range


    else:

    for bomb in bombs:
        etonations.append(1)
    return sum(detonations)

bombs=[
    [0,0,3],
    [2,1,2],
    [4,1,3],
    [9,3,2]
]

print(f"Bombs:{detonation(bombs)}")

# first: bombs
# second: product(roman, binary)
# 3rd: influencedNodes Social Network Influence Spread
# Input:
n = 6
edges = [[0,2], [1,2], [2,3], [2,4], [3,5], [4,5], [1,3], [0,4]]
k = 2
initial = [0,1]

output: 6

# 4th: jo ken po card game
deck = ["scissors", "stone", "paper", "..."]

Calculate the highest score

