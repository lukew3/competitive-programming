
def findSol(n, a):

    lastBest = a[0]
    bestArray = []
    lastItem = 0
    sectionIsPositive = False
    for item in a:
        if sectionIsPositive == False:
            if item>0:
                if item>lastBest:
                    lastBest = item
            else:
                bestArray.append(lastBest)
                sectionIsPositive = True
                lastBest = item
        elif sectionIsPositive == True:
            if item<0:
                if item>lastBest:
                    lastBest = item
            else:
                bestArray.append(lastBest)
                sectionIsPositive = False
                lastBest = item
    #bestArray.append(lastItem)
    print(bestArray)
    return sum(bestArray)



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(findSol(n, a))
