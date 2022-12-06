import sys
from collections import deque

for line in sys.stdin:
    q = deque()
    for i in range(len(line)):
        if len(q) < 4:
            q.append(line[i])
        else:
            q.append(line[i])
            q.popleft()
            if len(set(q)) == len(q):
                print(q)
                print(i+1)
                break

