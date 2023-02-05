import sys
sys.setrecursionlimit(10000)

rows, columns = map(int, input().split())

entrances = 0
visited = set()
entrance_set = {'X', ' ', '.'}

arr = []
for _ in range(rows):
    arr.append([char for char in input()])

def search(r, c):
    dot_found = False
    if (r, c) in visited:
        return
    elif arr[r][c] == 'X':
        return
    elif arr[r][c] not in entrance_set:
        # arr[r][c] = 'X'
        return
    elif arr[r][c] == '.':
        arr[r][c] = ' '
        dot_found = True

    #print(r, c)
    visited.add((r, c))

    if r > 0:
        dot_found = search(r - 1, c) or dot_found
    if r < rows - 1:
        dot_found = search(r + 1, c) or dot_found
    if c > 0:
        dot_found = search(r, c - 1) or dot_found
    if c < columns - 1:
        dot_found = search(r, c + 1) or dot_found
    
    return dot_found

for r in range(rows):
    for c in range(columns):
        if arr[r][c] not in entrance_set:
            arr[r][c] = ' '
            if search(r, c):
                entrances += 1

ssum = 0
for row in arr:
    for char in row:
        if char == '.':
            ssum += 1

print(entrances, ssum)