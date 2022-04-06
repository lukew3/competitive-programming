n = int(input())
branches = {}
for _ in range(n):
    a, b = map(int, input().split())
    branches[a] = b

maxLen = 0
parsed = []
node = 0
length = 0
for branch in sorted(branches):
    if branch not in parsed:
        length += 1
        node = branches[branch]
    else:
        if length > maxLen:
            maxLen = length


