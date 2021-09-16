import time
start_time = time.time()

def findSol(n):
    if ((n/2)%2)==1:
        print("NO")
        return []
    else:
        print("YES")
    left = 0
    right = 0
    solString = ""
    solArr = []
    ran1 = int(n/2)
    num = 0
    for l in range(ran1):
        num+=2
        left += num
        solString += str(num)+" "
        solArr.append(num)
    ran2 = ran1-1
    num = -1
    for r in range(ran2):
        num += 2
        right += num
        solString += str(num)+" "
        solArr.append(num)
    solString += str(int(left-right))
    solArr.append(int(left-right))
    return solArr

if __name__ == "__main__":
    #start_time = time.time()
    t = int(input())
    for _ in range(t):
        n = int(input())
        answer = findSol(n)
        if answer != "":
            print(answer)
            print(len(answer))
            print("--- %s seconds ---" % (time.time() - start_time))
