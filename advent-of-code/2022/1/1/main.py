import sys

maxx = 0
cur = 0
for line in sys.stdin:
    if line == '\n':
        if cur > maxx:
            maxx = cur
        cur = 0
    else:
        cur += int(line)
if cur > maxx:
    maxx = cur
print(maxx)
