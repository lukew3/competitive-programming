n = int(input())
l = []
while len(l) < n:
    l += [int(i) for i in input().split()]


ans = 0
count, maxCount = 0, 0
# s, e = 0, 0
# sm, em = 0, 0
e, em = 1, 1

for i in range(min(l), max(l) + 1):
    count = 0
    maxCount = 0
    for j in range(n):
        if l[j] >= i:
            count += 1
        else:
            if maxCount < count:
                maxCount = count
            # s = j - count
            e = j
            count = 0
    if maxCount < count:
        maxCount = count
        # s = j - count
        e = n
    # ans = max(ans, (maxCount + 1) * i)
    # print(ans)
    if ans < maxCount * i:
        ans = maxCount * i
        em = e
        sm = e - maxCount + 1
    if ans == maxCount * i:
        if sm > e - maxCount + 1:
            sm = e - maxCount - 1
            em = e
        # sm = min(sm, e - maxCount + 1)

print(sm, em, ans)