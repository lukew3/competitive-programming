cl = {
    'upper': '1',
    'middle': '2',
    'lower': '3'
}

t = int(input())
for _ in range(t):
    d = {}
    n = int(input())
    for _ in range(n):
        l = input().split()
        name = l[0][:-1]
        s = l[1].split('-')
        r = ''
        for c in s:
            r = cl[c] + r
        r = r + (10-len(r)) * '2'
        d[name] = r
        #print(name, r)
    out = sorted(d.keys(), key=lambda v: (d[v], v))
    for person in out:
        print(person)
    print('==============================')
