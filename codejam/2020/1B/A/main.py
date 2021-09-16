def decimalToBinary(n):
    return bin(n).replace("0b", "")

def checkPossible(x, y):
    if x%2 != 0 and y%2 != 0:
        return False
    else:
        return True
"""
def calcPath(x, y):
    xBin = list(decimalToBinary(abs(x)))
    yBin = list(decimalToBinary(abs(y)))
    print(xBin)
    print(yBin)

def bruteCalcPath(x,y):
    pass
"""
"""
def basicPath(x, y):
    targetReached = False
    i = 1
    while targetReached == False:
        jumpDist = 2**(i-1)
        print(jumpDist)
        if jumpDist == 4:
            targetReached = True
        i+=1
    return("N")
"""
def basicPath(x, y):
    targetReached = False
    i = 1
    while targetReached == False:
        jumpDist = 2**(i-1)
        print(jumpDist)
        if jumpDist == 4:
            targetReached = True
        i+=1
    return("N")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        print(checkPossible(x, y))
        if checkPossible(x, y):
            print(basicPath(x, y))
        else:
            print("IMPOSSIBLE")
        #print(x)
        #print(y)
