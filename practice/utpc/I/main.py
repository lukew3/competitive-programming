def calc_ops(subarr):
    ops = 0
    left_count = 1
    right_count = 1
    while len(subarr) != 0:
        if subarr[0]*left_count < subarr[-1]*right_count:
            ops += subarr.pop(0) * left_count
            left_count += 1
        else:
            ops += subarr.pop(-1) * right_count
            right_count += 1
    return ops

n, k = map(int, input().split())
s = sorted([int(i) for i in input().split()])
diffs = [s[i] - s[i-1] for i in range(1, n)]
best_diff = calc_ops(diffs[0:k-1])
for i in range(k,n):
    diff = calc_ops(diffs[i-k+1:i])
    if diff < best_diff:
        best_diff = diff
print(best_diff)
