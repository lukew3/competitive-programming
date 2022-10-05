t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    n -= 2
    flr = 1
    while n >= 0:
        n -= x
        flr += 1
    print(flr)


