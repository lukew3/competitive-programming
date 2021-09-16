import numpy as np
from scipy import linalg

t = int(input())
for i in range(t):
    x1, y1, x3, y3 = map(int, input().split())
    n = int(input())
    gm = -1000 #greatest slope
    x2 = 0
    y2 = 0
    if n == 0:
        yv = max(y1, y3)
        print(yv)
    else:
        for j in range(n):
            xt, yt = map(int, input().split())
            m = (y1-yt)/(x1-xt)
            if m > gm:
                gm = m
                x2 = xt
                y2 = yt
        l = np.array([[x1**2, x1, 1],[x2**2, x2, 1],[x3**2, x3, 1]])
        r = np.array([y1, y2, y3])
        s = linalg.solve(l, r)
        xv = -s[1]/(2*s[0]) #-b/(2a)
        yv = s[0]*(xv**2)+s[1]*xv+s[2]
        print(yv)

"""
Find the obstacle that lies on the parabola line
    If no obstacle, the height is the starting height or the gorilla's height (whichever is tallest)
https://socratic.org/questions/how-do-you-find-the-quadratic-function-y-ax-2-bx-c-whose-graph-passes-through-th
Gaussian elimination
"""
