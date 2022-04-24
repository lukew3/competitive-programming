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
    for c in cust:
        c.sort()
        for item in c:
            presses += abs(item - last)
            print(abs(item-last))
            last = item
    return presses

t = int(input())
for i in range(t):
    print(f"Case #{i+1}: {solve()}")

