
#INCOMPLETE
import itertools

def main():
    numCases = int(input())
    for case in range(numCases):
        n, k = map(int, input().split())
        print(n, k)
        traces = possibleTraces(n, k)
        #print(traces)
        squares = makeSquares(traces, n, k)
        #tracePerms(n)
        #print(squares)
"""
def makeSquares(n):
    baseSquare = []
    for i in range(n):
        baseSquare.append(i)
    squares = list(itertools.permutations(baseSquare))
    print(squares)
"""
def possibleTraces(n, k):
    baseTrace = []
    for i in range(1, n+1):
        baseTrace.append(i)
    traces = list(itertools.combinations_with_replacement(baseTrace, n)) #doesnt work, only gets traces without repeats
    goodTraces = []
    for trace in traces:
        result = sum(trace)
        if result == k:
            goodTraces.append(trace)
    return goodTraces


def makeSquares(traces, n, k):
    squares = []
    for trace in traces:
        square = []
        index = 0
        #add zeros and trace contents to square
        for num in trace:
            row = []
            for i in range(n):
                if i==index:
                    row.append(num)
                else:
                    row.append(0)
            index += 1
            square.append(row)
            #print(row)
        print(square)
        #add other numbers

        for row in square:
            colNum = 0
            for item in row:

                colNum += 1
        squares.append(square)
        print(square)
    return squares


#impossible if all but one number in trace is the same
#possible if all numbers are the same

def catchError(square, n, k):
    for row in square:
        if #duplicates found then return the
main()
