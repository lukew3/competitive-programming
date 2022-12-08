import sys
from collections import deque

grid = []
for line in sys.stdin:
    grid.append([int(i) for i in line[:-1]])

max_score = 0

rows = len(grid)
cols = len(grid)
for i in range(1, rows-1):
    for j in range(1, cols-1):
        print('---')
        h = grid[i][j]
        score = 1
        # left
        depth = 0
        for k in range(1, j+1):
            depth += 1
            if grid[i][j-k] >= h:
                break
        print(depth)
        score *= depth
        # right
        depth = 0
        for k in range(j+1, cols):
            depth += 1
            if grid[i][k] >= h:
                break
        print(depth)
        score *= depth
        # up
        depth = 0
        for k in range(1, i+1):
            depth += 1
            if grid[i-k][j] >= h:
                break
        print(depth)
        score *= depth
        depth = 0
        for k in range(i+1, rows):
            depth += 1
            if grid[k][j] >= h:
                break
        print(depth)
        score *= depth
        print(score)
        max_score = max(max_score, score)
print(max_score)

