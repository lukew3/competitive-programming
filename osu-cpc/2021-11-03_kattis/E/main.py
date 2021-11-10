import math

def solve(p, g, d, o):
    o = math.radians(o)
    a = g * math.cos(o)
    if a == 0:
        return p
    t = (-p + math.sqrt(p**2+2*a*d))/a
    if t < 0:
        t = (-p - math.sqrt(p**2+2*a*d))/a
    v = p + a*t
    return v

l = []
myin = input().split()
n = int(myin[0])
g = float(myin[1])
prev = 0
for _ in range(n):
    myin = input().split()
    d = float(myin[0])
    o = float(myin[1])
    l.append([d, o])

ol = []
for i in range(len(l)):
    prev = solve(prev, g, l[len(l)-1-i][0], l[len(l)-1-i][1])
    ol.append(prev)

for i in range(len(ol)):
    print(round(float(ol[len(ol)-1-i]), 5))

