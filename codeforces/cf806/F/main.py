t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    v = 0
    for i in range(n):
        if i+1 <= a[i]:
            continue
        for j in range(i+1, n):
            if a[j] <= i+1 or j+1 <= a[j]:
                continue
            v += int(a[j] > i+1)
    print(v)

