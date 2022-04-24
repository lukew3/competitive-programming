t = int(input())
for i in range(t):
    e, w = map(int, input().split())
    ops = 0
    sets = []
    for _ in range(e):
        sets.append([int(j) for j in input().split()])
    print(f"Case #{i+1}: {solve(input())}")

#BBA
