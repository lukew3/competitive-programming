
def findSol(n, a):
    bestArray = []
    greatestType = a[0]
    for i in range(n):
        item = a[i]
        if greatestType<0 and item<0:
            if item>greatestType:
                greatestType = item
        elif greatestType>0 and item>0:
            if item>greatestType:
                greatestType = item
        else:
            bestArray.append(greatestType)
            i-=1
            greatestType=item
    print(bestArray)
    return sum(bestArray)



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(findSol(n, a))
