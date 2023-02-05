n, r = map(int, input().split())

m = [int(input()) for _ in range(r)]
# print(m)
l = n * [0]
for i in range(1, n + 1):
    curr = i
    for j in m:
        if curr == j:
            curr += 1
        elif curr == j + 1:
            curr -= 1
    # print(i, curr)
    l[curr-1] = i

for i in l:
    print(i)
# print(l)
