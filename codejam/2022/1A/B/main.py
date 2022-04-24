t = int(input())
for _ in range(t):
    n = int(input())
    s = "1 1"
    last = 1
    sarr = [1,1]
    for i in range(n-2):
        sarr.append(s[-2] + s[-1])
        s += " " + str(i+1)
    print(s[:-1])
