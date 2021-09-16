def tid(in_list, k):
    out = []
    list2 = in_list
    for i in range(k):
        out.append(in_list.index(max(list2)))
        list2[list2.index(max(list2))] = 0
    return out

n, k = map(int, input().split())
t = [[], [], []]
for i in range(n):
    a, d, h = map(int, input().split())
    t[0].append(a)
    t[1].append(d)
    t[2].append(h)
print(len(set(tid(t[0], k) + tid(t[1],k) + tid(t[2],k))))
