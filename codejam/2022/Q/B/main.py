def solution():
    p1 = [int(j) for j in input().split()]
    p2 = [int(j) for j in input().split()]
    p3 = [int(j) for j in input().split()]
    sol = [0,0,0,0]
    for k in range(4):
        sol[k] = min(min(p1[k], p2[k]), p3[k])
        total = sol[0]+sol[1]+sol[2]+sol[3]
        if (total >= 10**6):
            sol[k] -= total - 10**6
            print(f"Case #{i+1}: {sol[0]} {sol[1]} {sol[2]} {sol[3]}")
            return
    print(f"Case #{i+1}: IMPOSSIBLE")

t = int(input())
for i in range(t):
    solution()
