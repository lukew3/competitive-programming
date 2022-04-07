import sys

mat = []
bestIndices = []
for line in sys.stdin:
    mat.append([int(i) for i in line.split()])
    bestIndices.append(mat[-1].index(max(mat[-1])))

solved = false
while not solved:
    if len(set(bestIndices)) == len(bestIndicess):




#find best in row
# check next row and if in same column, test second best in first row
