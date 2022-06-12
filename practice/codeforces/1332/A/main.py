#https://codeforces.com/contest/1332/problem/A
def main():
    case = 0
    cases = 0
    lineNum = 0
    cases = int(input())
    for i in range(0, cases):
        a, b, c, d = map(int, input().split())
        x, y, x1, y1, x2, y2 = map(int, input().split())
        if possibleWalk(a,b,c,d,x,y,x1,y1,x2,y2):
            print("Yes")
        else:
            print("No")

def possibleWalk(a,b,c,d,x,y,x1,y1,x2,y2):
    netx = b-a
    nety = d-c
    maxx = x2-x
    minx = x1-x
    maxy = y2-y
    miny = y1-y
    if (x1 == x2 and a+b > 0) or (y1 == y2 and c+d > 0):
        return False
    if (netx <= maxx and netx >= minx) and (nety <= maxy and nety >= miny):
        return True
    else:
        return False

main()
