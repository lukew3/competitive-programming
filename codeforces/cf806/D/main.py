t = int(input())
for _ in range(t):
    n = int(input())
    s = [''] * n
    b = ["0"] * n
    for i in range(n):
        s[i] = input()
    s.sort()
    print(s)
    for i in range(j, n):
        for j in range(n):
            if i != j and i != k and s[i] == s[j] + s[k]:
                b[i] = "1"
    print(''.join(b))
