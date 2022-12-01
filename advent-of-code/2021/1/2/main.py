import sys

data = [int(i) for i in sys.stdin]
c = -1
last = 0
for i in range(2, len(data)):
    val = data[i] + data[i-1] + data[i-2]
    if val > last:
        c += 1
    last = val
print(c)

