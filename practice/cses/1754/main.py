t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    d = abs(a-b)
    while a!=0 or b!=0:
        if a > b:
            a -= 2
            b -= 1
        else:
            a -= 1
            b -= 2
    if a == 0 and b == 0:
        print("YES")
    else:
        print("NO")
