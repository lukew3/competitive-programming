import math

i, j = map(int, input().split())
a = [int(i) for i in input().split()]
count = 0
myset = {}
for item in a:
    sol = int(item/j)
    if sol in myset:
        myset[sol] += 1
    else:
        myset[sol] = 1
for key in myset:
    item = myset[key]
    if item != 1:
        count += math.factorial(item)/(math.factorial(item-2)*2)

print(int(count))
