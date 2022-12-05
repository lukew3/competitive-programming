import sys
from collections import deque

s = [deque() for i in range(10)]
buildingStacks = True # boolean stating which mode we are in
for line in sys.stdin:
    if buildingStacks:
        if line == '\n': 
            buildingStacks = False
            continue
        for i in range(len(line)):
            if line[i] not in [' ', '[', ']', '\n']:
                if line[i].isnumeric(): continue
                index = i // 4 + 1
                s[index].appendleft(line[i])
    else:
        cmd = line.split()
        for i in range(int(cmd[1])):
            s[int(cmd[5])].append(s[int(cmd[3])].pop())
for q in s:
    if len(q) != 0:
        print(q.pop(), end='')
print()
