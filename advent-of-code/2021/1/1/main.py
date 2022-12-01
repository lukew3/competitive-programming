import sys

c = -1
last = 0
for line in sys.stdin:
    val = int(line)
    if val > last:
        c += 1
    last = val
print(c)

