n = int(input())
l = set()
for _ in range(n):
    word = input().lower().replace('-', ' ')
    if word not in l:
        l.add(word)
print(len(l))
