n = int(input())
w = {}
found = set()
c = 0
for _ in range(n):
    u = input().split()
    if u[0] not in w:
        w[u[0]] = u[1:]
    else:
        w[u[0]] += u[1:]
for key in w:
    for item in w[key]:
        if item not in w:
            if item not in found:
                c+=1
                found.add(item)
print(c)
