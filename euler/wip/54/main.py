import sys
def score(cards):
    high = 0
    for card in cards:
        if 
p1wins = 0
for line in sys.stdin:
    p1 = line.split()[:5]
    p2 = line.split()[5:]
    if score(p1) > score(p2):
        p1wins += 1
