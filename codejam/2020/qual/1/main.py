def main():
    numCases = int(input())

    for i in range(numCases):
        n = int(input())
        mainArray = []
        for j in range(n):
            rowContent = input().split()
            mainArray.append(rowContent)
        t = calcTrace(mainArray, n)
        r = calcRepRows(mainArray, n)
        c = calcRepCols(mainArray, n)
        print("Case #" + str(i+1) + ": " + str(t) + " " + str(r) + " " + str(c))

def calcTrace(myArray, size):
    trace = 0
    for i in range(size):
        trace += int(myArray[i][i])
    return trace

def calcRepRows(myArray, size):
    r = 0
    for i in range(size):
        hasDup = True
        rowList = myArray[i]
        if len(set(rowList)) == len(rowList):
            hasDup = False
        else:
            hasDup = True
            r += 1
    return r

def calcRepCols(myArray, size):
    c = 0
    for i in range(size):
        hasDup = True
        colList = []
        for j in range(size):
            colList.append(myArray[j][i])
        if len(set(colList)) == len(colList):
            hasDup = False
        else:
            hasDup = True
            c += 1
    return c

main()
