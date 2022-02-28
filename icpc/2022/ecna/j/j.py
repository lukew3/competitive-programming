n = int(input())
l = []
while len(l) < n:
    l += [int(i) for i in input().split()]

maxArea = 0
maxStart = 0
maxEnd = 0
for i in range(min(l), max(l) + 1):
    if i not in l:
        continue

    currIntSize = 0
    intSize = 0
    endIndex = 0
    for j in range(n):
        if l[j] >= i:
            currIntSize += 1
            if intSize < currIntSize:
                intSize = currIntSize
                endIndex = j
        else:
            currIntSize = 0
    startIndex = endIndex - intSize + 1
    area = intSize * i

    if maxArea < area:
        maxArea = area
        maxStart = startIndex
        maxEnd = endIndex
    if maxArea == area and startIndex < maxStart:
        maxStart = startIndex
        maxEnd = endIndex


print(maxStart + 1, maxEnd + 1, maxArea)

        
