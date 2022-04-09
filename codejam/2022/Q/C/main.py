t = int(input())
for i in range(t):
    n = int(input())
    d = [int(j) for j in input().split()]
    d = sorted(d)
    first = d[0]
    last = d[0]
    for k in range(1, len(d)):
        if d[k] > last:
            last += 1
        elif first > 1:
            first -= 1
    print(f"Case #{i+1}: " + str(last-first+1))
