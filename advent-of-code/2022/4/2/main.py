import sys

s = 0
for line in sys.stdin:
    a = line[:-1].split(',')
    a1 = [int(i) for i in a[0].split('-')]
    a2 = [int(i) for i in a[1].split('-')]
    if (a1[0]<=a2[0] and a1[1] >= a2[0]) or (a2[0]<=a1[0] and a2[1]>=a1[0]):
        s += 1
print(s)
