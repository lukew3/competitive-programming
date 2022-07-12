t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    for i in range(n):
        s = input().split()[1][::-1]
        for op in s:
            if op == 'D':
                if a[i] == 9:
                    a[i] = 0
                else:
                    a[i] += 1
            else:
                if a[i] == 0:
                    a[i] = 9
                else:
                    a[i] -= 1
    for item in a:
        print(item, end=' ')
    print()

