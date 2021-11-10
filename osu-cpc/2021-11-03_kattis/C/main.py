def solve(n):
    nums = []
    for _ in range(n):
        nums.append(input())
    nums.sort()
    i = 0
    while i < n:
        j = i+1
        while j < n:
            if nums[i] < nums[j][:len(nums[i])]:
                break
            elif nums[i] == nums[j][:len(nums[i])]:
                return "NO"
            j+=1
        i+=1
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
