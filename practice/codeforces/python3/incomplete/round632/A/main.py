def findGoodPainting(n, m):
    bSq = 0
    wSq = 0
    painting = [ [ None for i in range(m) ] for j in range(n) ]

    lastSquare = "W"
    for i in range(n):
        for j in range(m):
            thisSquare = "O"
            if lastSquare == "W":
                thisSquare = "B"
                bSq+=1
            elif lastSquare == "B":
                thisSquare = "W"
                wSq+=1
            lastSquare = thisSquare
            painting[i][j] = thisSquare

    fixed = False
    if bSq == wSq:
        for i in range(n):
            for j in range(m):
                if painting[i][j]=="W":
                    if (i+1>=n or painting[i+1][j]!="W") and (i-1<=n or painting[i-1][j]!="W") and (j+1>=m or painting[i][j+1]!="W") and (j-1<=m or painting[i][j-1]!="W"):
                        painting[i][j]="B"
                        fixed=True
                        break
            if fixed==True:
                break
    return painting

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        painting = findGoodPainting(n, m)
        for i in range(n):
            lineString = ""
            for j in range(m):
                lineString += painting[i][j]
            print(lineString)
