set_n = 1
n = int(input())
while n != 0:
    top = []
    bottom = []
    for _ in range(n // 2):
        top.append(input())
        bottom.append(input())
    if n % 2 == 1:
        top.append(input())
    top = sorted(top, key=lambda item: len(item))
    bottom = sorted(reversed(bottom), key=lambda item: len(item), reverse=True)
    print(f"SET {set_n}")
    for item in top:
        print(item)
    for item in bottom:
        print(item)
    n = int(input())
    set_n += 1
