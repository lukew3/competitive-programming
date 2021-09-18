t = input()
for i in range(int(t)):
    d, n, k = map(int, input().split())
    days = []
    for z in range(d):
        days.append([])
    for _ in range(n):
        h, s, e = map(int, input().split())
        for j in range(s-1, e):
            if len(days[j]) < k:
                days[j].append(h)
            else:
                m = min(days[j])
                if h > m:
                    days[j].remove(m)
                    days[j].append(h)
    mfun = 0
    for l in range(d):
        dfun = 0
        for item in days[l]:
            dfun += item
        if dfun > mfun:
            mfun = dfun
    print(f"Case #{i+1}: {str(mfun)}")
