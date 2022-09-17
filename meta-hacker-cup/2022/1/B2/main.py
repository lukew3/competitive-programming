def solve():
    total_sum = 0

    x_sum = 0
    y_sum = 0
    xy_squared_sum = 0

    n = int(input()) # number of trees
    for _ in range(n):
        x, y = map(int, input().split())
        x_sum += x
        y_sum += y
        xy_squared_sum += x ** 2 + y ** 2
    q = int(input()) # number of wells
    for _ in range(q):
        wx, wy = map(int, input().split())
        total_sum += n * (wx**2 + wy**2)
        total_sum += -2 * (wx * x_sum + wy * y_sum)
    return (total_sum + q * xy_squared_sum) % 1000000007

t = int(input())
for case_num in range(1, t+1):
    print(f"Case #{case_num}: {solve()}")

