n = int(input())
d = int(len(str(n)))

t = 0
for i in range(d):
    l = 10 ** i
    u = 10 ** (i+1)
    if u > n:
        u = n+1
    s = int(((u-l)*((u-l)+1))/2)
    t += s

t %= 998244353

print(t)
