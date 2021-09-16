
def countGood(a, aLen):
    goodCount = 0
    constArray = a.copy()
    subArray = constArray.copy()
    for c in range(aLen): #take a off the front
        del subArray[0]
        #print(subArray)
        for d in range(len(subArray)):#take b off the back
            del subArray[(len(subArray)-1)]
            #print(subArray)
            if checkGood(subArray)==True:
                print(subArray)
                goodCount+=1
        subArray = constArray.copy()
        for _ in range(c):
            del subArray[0]
    return goodCount

def checkGood(subArray):
    isGood = True
    constantArray = subArray.copy()
    sub = constantArray.copy()
    for a in range(len(sub)): #take a off the front
        del sub[0]
        for b in range(len(sub)):#take b off the back
            del sub[(len(sub)-1)]
            if sum(sub)==0:
                isGood=False
        sub = constantArray.copy()
        for _ in range(a):
            del sub[0]
    return isGood

if __name__ == "__main__":
    aLen = int(input())
    a = list(map(int, input().split()))
    print(countGood(a, aLen))
