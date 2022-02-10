n = int(input())
l = input().split()
rl = [0]
a = 0
for item in l:
    a += int(item)
    if a >= 360:
        a-=360
    rl.append(a)

rl = sorted(rl)
g = 360 - rl[-1]
for i in range(len(rl)-1):
    d = rl[i+1] - rl[i]
    if d > g:
        g = d

print(g)
