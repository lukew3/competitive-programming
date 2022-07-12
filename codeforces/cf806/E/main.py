import math

t = int(input())
for _ in range(t):
    n = int(input())
    g = []
    ops = 0
    for _ in range(n):
        g.append([bool(int(char)) for char in input()])
    for i in range(math.ceil(n/2)):
        for j in range(math.floor(n/2)):
            s = 0
            s += int(g[i][j])
            s += int(g[j][n-i-1])
            s += int(g[n-i-1][n-j-1])
            s += int(g[n-j-1][i])
            ops += min(4-s, s)
    print(ops)
