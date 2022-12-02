import sys

top = [0, 0, 0]
cur = 0
for line in sys.stdin:
    if line == '\n':
        if cur > top[0]:
            top[0] = cur
            top.sort()
        cur = 0
    else:
        cur += int(line)
if cur > top[0]:
    top[0] = cur
print(sum(top))
