#https://codeforces.com/problemset/problem/1008/B
numrects = int(input())
lastmax = -1
possible = False
hless = False
wless = False
for i in range(0,numrects):
    w, h = map(int, input().split())
    if (lastmax == -1) or ((h <= lastmax) and (w <= lastmax)) :
        possible = True
        if h>w:
            lastmax = h
        else:
            lastmax = w
    elif (h <= lastmax) and not (w <= lastmax):
        possible = True
        lastmax = h
    elif (w <= lastmax) and not (h <= lastmax):
        possible = True
        lastmax = w
    else:
        possible = False
        break
if possible:
    print("YES")
else:
    print("NO")
