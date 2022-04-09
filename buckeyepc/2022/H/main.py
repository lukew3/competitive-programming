data = []
def findBest(x, y, curScore, last):
    if data[y][x] <= last:
        return -1001
    a = -1
    b = -1
    if x < n-1:
        #try next right
        moved = True
        a = findBest(x+1,y,curBest)
    if x > 0:
        #try next left 
        moved = True
        b = findBest(x+1,y,curBest)
    if y < m-1:
        #try next bottom 
        moved = True
        c = findBest(x+1,y,curBest)
    d = max(max(a,b),c)
    if d == -1001:
        return -1001
    else:
        return curScore + d

n, m = map(int, input().split())
for _ in range(m):
    data.append([int(i) for i in input().split()])

print(findBest(0,0,1,-1001))
