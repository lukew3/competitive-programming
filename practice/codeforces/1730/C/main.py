def solve():
    s = input()
    digCount = {}
    for char in s:
        if char in digCount:
            digCount[char] += 1
        else:
            digCount = 1

    pass

t = int(input())
for _ in range(t):
    solve()
