data = []
def findBest(x, y, curBest):
    moved = False
    a = -1
    b = -1
    if x < n-1:
        #try next right
        moved = True
        a = findBest(x+1,y,curBest)
    if y < m-1:
        #try next right
        moved = True
        b = findBest(x+1,y,curBest)

        
    pass

n, m = map(int, input().split())
for _ in range(m):
    data.append([int(i) for i in input().split()])

print(findBest(0,0,1))
