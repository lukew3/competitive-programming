def calcPath(n):
    path = []
    if n<=5:
        for i in range(1, n+1):
            path.append([i,i])
    else:
        path = [[1,1],[2,2],[3,3]]
        row=3
        sum=3
        lastVal = 1
        print("val: " + str(sum))
        while sum+(lastVal+row-2)+(row) < n:
            row+=1
            currentVal = lastVal+row-2
            sum+=currentVal
            print("val: " + str(currentVal))
            print("sum: " + str(sum))
            path.append([row, 3])
            lastVal = currentVal
        #print(row)
        #print(sum)
        while sum+(row-1) < n:
            row+=1
            currentVal = row-2
            sum+=currentVal
            print("val: " + str(currentVal))
            print("sum: " + str(sum))
            path.append([row-1, 2])
        while sum < n:
            row+=1
            sum+=1
            print("val: " + str(1))
            print("sum: " + str(sum))
            path.append([row-2, 1])
        print(sum)
    return path

def printPath(path, case):
    print("Case #" + str(case) + ":")
    for part in path:
        myStr = ""
        myStr+= str(part[0]) + " "
        myStr+= str(part[1])
        print(myStr)

if __name__ == "__main__":
    t = int(input())
    for k in range(t):
        n = int(input())
        printPath(calcPath(n), k+1)
