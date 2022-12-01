import math

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
d1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
d2 = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
# Distance between roots
d3 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

if d3 < d1 + d2:
    print("Yes")
else:
    print("No")

