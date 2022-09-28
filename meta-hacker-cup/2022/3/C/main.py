def solve():
    n, k = map(int, input().split())
    c0, w0 = map(int, input().split())
    count_heavier = 0
    count_lighter = 0
    for _ in range(n-1):
        c, w = map(int, input().split())
        if w > w0:
            count_heavier += c
        else:
            # same weight does the same as lighter since you throw left if right is lighter or equal
            count_lighter += c

    # Find the probability that you pick up batch one at least once # c0/c_h+c_l
    # AND 
        # you didn't pick up a lighter cookie
        # OR that you weigh a heavier cookie each time

    p = 1
    q = 1
    d = c0 / (count_heavier + count_lighter) + 
    # prob of at least one choc
    # actually prob of being raisin every time
    for i in range(k):
        d += c0 / (count_heavier + count_lighter - i)
    p = q - p
    # prob of heavier than choc every time
    """
    for i in range(k):
        p *= count_heavier
        q *= (count_heavier + count_lighter)
        count_heavier -= 1
    """
    print(d)
    print(p, '/', q)


t = int(input())
for case_num in range(t):
    print(f"Case #{case_num+1}: {solve()}")
