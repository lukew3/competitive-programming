t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    s = ['B'] * m
    for op in a:
        minn = min(op-1, m-op)
        maxx = max(op-1, m-op)
        if s[minn] != 'A':
            s[minn] = 'A'
        else:
            s[maxx] = 'A'
    print(''.join(s))
