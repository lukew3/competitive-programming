import random

def simgame(l, t):
    pos = 1
    rc = 0
    while True:
        pos += random.randint(1, 6)
        rc += 1
        for ladder in l:
            if ladder[0] == pos:
                pos = ladder[1]
                break
        if pos >= t:
            return rc

def solve(t, l, p):
    games = 1000000
    gamelist = []
    for _ in range(games):
        gamelist.append(simgame(l, t))
    gamelist.sort()
    print(gamelist[int(games*p)])

def main():
    r, c, k = map(int, input().split())
    t = r * c #target
    p = float(input())
    l = []
    for _ in range(k):
        l.append(list(map(int, input().split())))
    solve(t, l, p)

main()
