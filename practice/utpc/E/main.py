n, m, f = map(int, input().split())
arr = [[-1 for i in range(n)] for i in range(n)]
print(arr)
d = {}
for _ in range(m):
    a, b, c = map(int, input().split())
    if arr[a][b] != -1:
        arr[a][b] = min(arr[a][b], c)
    else:
        arr[a][b] = c

best = [-1 for i in range(n)]
parsePath([1], [0])
def parsePath(touchedNodes, costs):
    lastNode = touchedNodes[-1]
    if best[lastNode] != -1:
        maxx = max(costs)
        best[lastNode] = min(
    # for each node in array
    for i in range(len(arr)):
        nextCost = arr[lastNode][i]
        if nextCost != -1 and i not in touchedNodes:
            parsePath(




