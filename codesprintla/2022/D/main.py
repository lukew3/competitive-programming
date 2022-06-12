import math

def solve():
    n, t = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(int(input()))
    s = sorted(s, reverse=True)

    k = t
    a = int(math.ceil(n/4))-1
    b = int(math.ceil(n/2))-1
    c = int(math.ceil(3*n/4))-1
    l = [int(s[a]/0.9), int(s[b]/0.8), int(s[c]/0.7)]
    k = min(l)
    if k == 0:
        return -1
    else:
        return k

print(solve())
