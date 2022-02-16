def main():
    n = int(input())
    c = [int(i) for i in input().split()]
    # must be an even number of odd stacks
    oddStacks = 0
    for stack in c:
        if stack % 2 == 1:
            oddStacks += 1

    if oddStacks % 2 == 1 or max(c) > sum(c)-max(c):
        print("no")
    else:
        print("yes")
        for _ in range(n-1):
            largestIndex = c.index(max(c))
            # set value at largestIndex to 0 temporarily
            largestValue = c[largestIndex]
            c[largestIndex] = 0
            secondLargestIndex = c.index(max(c))
            count = min(largestValue, c[secondLargestIndex])
            for _ in range(count):
                print(largestIndex+1, secondLargestIndex+1)
            c[largestIndex] = largestValue - count
            c[secondLargestIndex] -= count
main()    

