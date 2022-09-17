def solve():
    total_sum = 0

    n = int(input()) # number of trees
    trees = []
    for _ in range(n):
        trees.append([int(i) for i in input().split()])
    q = int(input()) # number of wells
    for _ in range(q):
        well = [int(i) for i in input().split()]
        for tree in trees:
            total_sum += (well[0] - tree[0])**2 + (well[1] - tree[1])**2
            if total_sum >= 1000000007:
                total_sum = total_sum % 1000000007
    return total_sum

t = int(input())
for case_num in range(1, t+1):
    print(f"Case #{case_num}: {solve()}")
