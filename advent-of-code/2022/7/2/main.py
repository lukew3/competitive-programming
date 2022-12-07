import sys
from collections import deque

d = {} # set containing dicts and their sizes
path = deque()
def addtod(n):
    p = ''
    for item in path:
        p += item
        d[p] += n

for line in sys.stdin:
    s = line.split()
    if s[0] == '$':
        if s[1] == 'cd':
            if s[2] == '..':
                p = path.pop()
            else:
                path.append(s[2])
                d[''.join(path)] = 0
    elif s[0] != 'dir':
        # For a given file, add that size to each dictionary it is found in
        addtod(int(s[0]))

smallest = d['/']
target = 30000000 - 70000000 + d['/']
for item in d:
    dirsize = d[item]
    if dirsize > target and dirsize < smallest:
        smallest = dirsize
print(smallest)

