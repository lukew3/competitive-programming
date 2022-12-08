import sys
from collections import deque

grid = []
for line in sys.stdin:
    grid.append([int(i) for i in line[:-1]])

grid2 = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
grid2[0] = [True for _ in range(len(grid[0]))]
grid2[-1] = [True for _ in range(len(grid[0]))]

# for every row
for i in range(1, len(grid)-1):
    tallest_from_right = -1
    tallest_from_left = -1
    l = len(grid[0])
    for j in range(len(grid[0])):
        if grid[i][j] > tallest_from_left:
            grid2[i][j] = True
            tallest_from_left = grid[i][j]
        if grid[i][l-1-j] > tallest_from_right:
            grid2[i][l-1-j] = True
            tallest_from_right = grid[i][l-1-j]

# for every column
for i in range(len(grid[0])):
    tallest_from_top = -1
    tallest_from_bottom = -1
    l = len(grid)
    for j in range(len(grid)):
        if grid[j][i] > tallest_from_bottom:
            grid2[j][i] = True
            tallest_from_bottom = grid[j][i]
        if grid[l-1-j][i] > tallest_from_top:
            grid2[l-1-j][i] = True
            tallest_from_top = grid[l-1-j][i]

print(grid2)
s = 0
for row in grid2:
    for col in row:
        s += col
print(s)

