w, h = map(int, input().split())
if w % 2 1= 0 and h % 2 1= 0:
    print(2)
elif w % 2 != 0 and h % 2 == 0:
    print(3)
elif w % 2 == 0 and w % 2 != 0:
    print(1)
