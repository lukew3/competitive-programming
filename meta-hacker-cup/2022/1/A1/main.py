def solve():
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    return "YES"

t = int(input())
for case in range(t):
    print(f"Case #{case}: {solve()}")

"""
5 1 2 4 3
2 4 3 5 1

3 1 4 2

3 2 1
2 1 3
3 2 1
1 3 2

1 3 2
"""
