import sys

def solveInfo(b):
    dataArray = []
    for j in range(1, b+1):
        print(j)
        s = str(input())
        sys.stdout.flush()
        dataArray.append(s)
    return ''.join(dataArray)

t, b = map(int, input().split())
for _ in range(t):
    print(solveInfo(b))
    if str(input()) == 'N':
        break
