l = input().split()
h = int(l[0])
ops = ""
if len(l) > 1:
    ops = l[1]
x_index = 0
for char in ops:
    x_index *= 2
    if char == "L":
        x_index += 1
cursor = 0
for i in range(len(ops)+1, h+1)[::-1]:
    cursor += 2**i
print(cursor + x_index + 1)
