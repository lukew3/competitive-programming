t = int(input())
for _ in range(t):
    n = int(input())
    # 2 every time?
    print(2)
    dups = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i, end=' ')
            i *= 2
            while i < n + 1:
                print(i, end=' ')
                i *= 2
    print()

# 1-2-4-8 3-6-12 5-10 7 9 11
