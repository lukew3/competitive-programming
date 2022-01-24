x, y = map(int, input().split())
n = int(input())
cx = 0
cy = 0

i = []
for _ in range(n):
    i.append(input())
    if i[-1] == "Forward":
        cy += 1
    else if i[-1] == "Right":
        cx += 1
    else if i[-1] == "Left":
        cx -= 1

