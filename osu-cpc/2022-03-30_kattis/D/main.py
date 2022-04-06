def solution(l):
    pass

c = int(input())
for i in range(c):
    l = [int(j) for j in input().split()]
    n = l.pop(0)
    print(f"Case #{i+1}: {solution(l)}")

