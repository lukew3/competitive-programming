t = int(input())
for _ in range(t):
    input()
    s = input()
    b = 0
    solves = []
    for char in s:
        if char not in solves:
            solves.append(char)
            b += 2
        else:
            b += 1
    print(b)
