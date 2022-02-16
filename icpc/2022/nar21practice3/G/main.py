n = int(input())
l = [int(i) for i in input().split()]
count = 0
for i in range(len(l)):
    if l[i] == 1:
        count2s = 0
        for j in range(i, len(l)):
            if l[j] == 2:
                count2s += 1
            elif l[j] == 3:
                value = 0
                for i in range(count2s):
                    value *= 2
                    value += 1
                count += value
print(count)

