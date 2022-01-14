def main():
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        return
    calls = []
    for _ in range(n):
        _, _, s, d = map(int, input().split())
        calls.append([s, s+d-1])
    intervals = []
    for _ in range(m):
        c = 0
        s, d = map(int, input().split())
        e = s + d - 1
        for call in calls:
            if (s <= call[0] and e >= call[1]) or (s >= call[0] and s <= call[1]) or (e <= call[1] and e >= call[0]):
                c+=1
        print(c)
    main()

main()
