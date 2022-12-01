n = int(input())
count = 0
days = [int(i) for i in input().split()]

dirty_days = 0
dirt = 0
for i in range(365):
    dirt += dirty_days

    if dirt >= 20:
        dirty_days = 0
        dirt = 0
        count += 1

    if len(days) > 0 and days[0] == i:
        days.pop(0)
        dirty_days += 1

if dirt != 0:
    count += 1

print(count)
