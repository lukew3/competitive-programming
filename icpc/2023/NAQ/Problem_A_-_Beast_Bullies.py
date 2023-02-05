# Strongest 4 vs next strongest 4
# After, the strongest will try to eliminate each other

# Only have to consider top 4 since the rest will be eliminated by the top group

n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
l.sort(reverse=True)

if len(l) > 4:
    l = l[:4]

# print(l)
if l[0] > sum(l[1:]):
    print(1)
else:
    print(3)