n, m = map(int, input().split())
a = []
for _ in range(n):
    l = input()
    a.append([int(l[char_i]) for char_i in range(len(l))])

print(a)
