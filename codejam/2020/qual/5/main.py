

#INCOMPLETE
def main():
    numCases = int(input())
    for case in range(numCases):
        n, k = map(int, input().split())
        squares = makeSquares(n)
        tracePerms(n)
        #print(squares)

def makeSquares(n):
    squares = []
    for i in range(n):
        square = []
        for k in range(n):
            row = ['1']
            square.append(row)
        #row = ['1']
        #square = [row]

        squares.append(square)
    return squares

def calcTrace(myArray, n):
    t = 0
    for j in range(n):
        t += int(myArray[j][j])
    return t

def tracePerms(n):
    tracePermsList = []
    lastPlace = 0
    while lastPlace != n:
        permGen(n)
        print("Broken")
    pass

def permGen(n):
    tracePerm = []
    last = 0
    for i in range(n):
        curDigit = i
        curPlace = 0
        if last == n:
            lastPlace = last
            break
        else:
            print(i)
            tracePerm.append(i)
            recursivePermGen(n, curPlace, tracePerm)
    print(tracePerm)

def recursivePermGen(n, last, thisPerm):
    for i in range(n):
        curDigit = i
        curPlace = last + 1
        if last == n:
            lastPlace = last
            break
        else:
            print(i)
            thisPerm.append(i)
            recursivePermGen(n, curPlace, thisPerm)
main()
