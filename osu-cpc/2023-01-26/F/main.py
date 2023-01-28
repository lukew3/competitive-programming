j = [int(i) for i in input().split()]
l = [0]
for _ in range(10):
    l.append([int(i) for i in input().split()])

t = 0
sset = 0
while sset != 30:
    item = l[sset % 10 + 1]
    if (t-item[2])%(item[0] + item[1]) >= item[0]:
        t += j[2 * (sset % 10)]
        l[sset % 10 + 1][2] = t
        t += j[2*(sset % 10) + 1]
        sset += 1
    else:
        t += 1

print(t - j[-1])
