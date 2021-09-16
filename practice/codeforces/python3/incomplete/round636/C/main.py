
def findSol(n, a):
    lastSign = False #false is negative true is positive
    lastBest = 0
    bestArray = []
    myIndex = 0
    for item in a:
        if myIndex == 0:
            lastBest = item
            if item < 0:
                lastSign = False
            elif item > 0:
                lastSign = True
        elif item < 0 and lastSign==False:
            if item > lastBest:
                lastBest = item
        elif item > 0 and lastSign==True:
            if item > lastBest:
                lastBest = item
        else:
            bestArray.append(lastBest)
            #if item < 0:
            #    lastSign = False
            #elif item > 0:
        #        lastSign = True
            lastBest = item
        myIndex+=1
    return sum(bestArray)



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(findSol(n, a))
