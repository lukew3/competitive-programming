def solve():
    c = int(input())
    l = [int(i) for i in input().split()]
    mindel = 0
    count = 0
    low_index = 0
    high_index = c-1
    for _ in range(c):
        if l[low_index] <= l[high_index] and l[low_index] >= mindel:
            mindel = max(l[low_index], mindel)
            count += 1
            low_index += 1
        elif l[high_index] < l[low_index] and l[high_index] >= mindel:
            mindel = max(l[high_index], mindel)
            count += 1
            high_index -= 1
        elif l[low_index] <= l[high_index]:
            mindel = max(l[low_index], mindel)
            low_index += 1
        elif l[high_index] < l[low_index]:
            mindel = max(l[high_index], mindel)
            high_index -= 1
    return count

t = int(input())
for i in range(t):
    print(f"Case #{i+1}: {solve()}")

