n = int(input())
l = []
while n != 0:
    for _ in range(n):
        l.append(input())
    print('\n'.join(sorted(l, key=lambda val: val[:2])))
    n = int(input())
    l = []
    print()
