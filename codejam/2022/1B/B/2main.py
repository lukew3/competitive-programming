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
    for i in range(n):
        c = cust[i]
        c.sort()
        # start at item closes to last pressure
        startIndex = 0
        bestDistance = last
        for j in range(p):
            dist = abs(c[j]-last)
            if dist < bestDistance:
                startIndex = j
                bestDistance = dist
            else:
                break
        if abs(c[startIndex]-c[0]) > abs(c[startIndex]-c[-1]):
            # go up first
            for k in range(startIndex,p):
                print(c[k])
                presses += abs(last-c[k])
                last = c[k]
            for k in reversed(range(0, startIndex)):
                print(c[k])
                presses += abs(last-c[k])
                last = c[k]
        else:
            # go down first
            for k in reversed(range(0, startIndex)):
                print(c[k])
                presses += abs(last-c[k])
                last = c[k]
            for k in range(startIndex,p):
                print(c[k])
                presses += abs(last-c[k])
                last = c[k]
    return presses

t = int(input())
for i in range(t):
    print(f"Case #{i+1}: {solve()}")

