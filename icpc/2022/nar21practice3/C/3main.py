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
        for i in range(n-1):
            count = min(c[i], c[i+1])
            for _ in range(count):
                print(i+1, i+2)
            c[i+1] -= count
main()
