
#INCOMPLETE
import sys

def checkAndChange(w, x, y, z, mainArray):
    w2 = requestServer(mainArray, 0)
    x2 = requestServer(mainArray, 1)
    y2 = requestServer(mainArray, b)
    z2 = requestServer(mainArray, b-1)
    if w2==w and x2==x and y2==y and z2==z:
        transformData(4, mainArray)
    elif w2!=w and x2!=x and y2!=y and z2!=z:
        transformData(1, mainArray)
    elif w2==y and x2==z and y2==w and z2==x:
        transformData(2, mainArray)
    else:
        transformData(3, mainArray)
    pass
def transformData(type, mainArray):
    location = -1
    if type == 1:
        for item in mainArray:
            location += 1
            if item == '1':
                mainArray[location] = '0'
            elif item == '0':
                mainArray[location] = '1'
    elif type == 2:
        mainArray = list(reversed(array))
    elif type == 3:
        mainArray = list(reversed(array))
        for item in mainArray:
            location += 1
            if item == '1':
                mainArray[location] = '0'
            elif item == '0':
                mainArray[location] = '1'
    else:
        pass

def requestServer(mainArray, l):
    print(l+1)
    s = str(input())
    sys.stdout.flush()
    mainArray[l] = s
    return s

def solveInfo(b):
    dataArray = [None] * b
    w=-1
    x=-1
    y=-1
    z=-1
    requestCount = 0
    for j in range(0, b):
        requestCount+=1
        if requestCount%10 == 1:
            checkAndChange(w,x,y,z, dataArray)
        requestServer(dataArray, j)
    return ''.join(dataArray)

t, b = map(int, input().split())
for _ in range(t):
    print(solveInfo(b))
    if str(input()) == 'N':
        break
