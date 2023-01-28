n = int(input())
l = [int(i) for i in input().split()]
s = 0
for item in l:
    if item != -1:
        s += item
    else:
        n -= 1
print(s/n)
