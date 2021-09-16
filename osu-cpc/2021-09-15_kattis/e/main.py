def tid(in_list, k):
    out = []
    list2 = in_list
    for i in range(k):
        out.append(in_list.index(max(list2)))
        list2[list2.index(max(list2))] = 0
    return out

n, k = input().split()
k = int(k)
ta = []
td = []
th = []
t = [[], [], []]
for i in range(int(n)):
    a, d, h = input().split()
    t[0].append(int(a))
    t[1].append(int(d))
    t[2].append(int(h))
top = tid(t[0], k) + tid(t[1],k) + tid(t[2],k)
top = set(top)
print(len(top))
