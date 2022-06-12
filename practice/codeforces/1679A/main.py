import math
t = int(input())
for _ in range(t):
    n = int(input())
    if n%2 != 0 or n==2:
        print(-1)
    else:
        minn = int(n/6)
        if n%6 != 0:
            minn+=1
        maxx = int(n/4)
        print(minn, maxx)
