def mine2e(c1, c2):
    # give the end of c1 that is closest to an en of c2
    pass

def solve():
    n, p = map(int, input().split())
    presses = 0
    cust = []
    for _ in range(n):
        cust.append([int(j) for j in input().split()])
    last = 0
    mm = []
    for c in cust:
        mm.append([min(c), max(c)])
    for i in range(n):
        cust[i].sort()
        """
        for item in c:
            presses += abs(item - last)
            print(abs(item-last))
            last = item
        """
        # start at item closes to last pressure
        startIndex = 0
        bestDistance = last
        for j in range(p):
            dist = abs(cust[i][j] - bestDistance)
            if dist < bestDistance:
                startIndex = j
                bestDistance = dist
            else:
                break
        del(bestDistance)
        # end at item closest to min or max pressure of next customer
          # first check that you can compare current customer to next customer
        if i != n-1:
            # go down first
            if min(abs(cust[i][-1]-mm[i+1][0]), abs(cist[i][-1]-mm[i+1][1])) <= min(abs(cust[i][0]-mm[i+1][0]), abs(cust[i][0]-mm[i+1][-1])):
                for i in range(c):



t = int(input())
for i in range(t):
    print(f"Case #{i+1}: {solve()}")

