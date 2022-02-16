def getQueue(c):
    t = c.copy()
    o = []
    for _ in range(len(t)):
        maxi = t.index(max(t))
        o.append(maxi)
        t[maxi] = 0
    return o

def main():
    n = int(input())
    c = [int(i) for i in input().split()]
    # must be an even number of odd stacks
    oddStacks = 0
    for stack in c:
        if stack % 2 == 1:
            oddStacks += 1

    if oddStacks % 2 == 1:
        print("no")
    else:
        print("yes")
        # sort biggest stacks
        o = getQueue(c)
        #take from the biggest stacks
        for i in range(n-1):
            print(c)
            print(o[i], o[i+1])
            count = min(c[o[i]], c[o[i+1]])
            print(count)
            for _ in range(count):
                print(o[i] + 1, o[i+1] + 1)
            c[o[i]] -= count
            c[o[i+1]] -= count

main()
"""
    while max(c) != 0:
        largestIndex = c.index(max(c))
        # set value at largestIndex to 0 temporarily
        largestValue = c[largestIndex]
        c[largestIndex] = 0
        secondLargestIndex = c.index(max(c))
        print(largestIndex+1, secondLargestIndex+1)
        c[largestIndex] = largestValue - 1
        c[secondLargestIndex] -= 1
"""
