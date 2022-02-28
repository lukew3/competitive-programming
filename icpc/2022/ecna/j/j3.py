n = int(input())

l = []
while len(l):
    
ans = 0
count, maxCount = 0, 0
s, e = 0, 0
sm, em = 0, 0
for i in range(min(l), max(l)):
    count = 0
    maxCount = 0
    for j in range(n):
        if l[j] >= i:
            count += 1
        else:
            if maxCount < count:
                maxCount = count
                s = j - count
                e = j + 1
            count = 0
    # ans = max(ans, (maxCount + 1) * i)
    print(ans)
    if ans < (maxCount + 1) * i:
        ans = (maxCount + 1) * i
        sm = s
        em = e

print(sm, em, ans)