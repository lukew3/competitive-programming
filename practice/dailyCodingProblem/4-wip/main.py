# Don't think that this solution is valid because it isn't linear time
# Also, doesn't work with duplicates
def solution(a):
    positives = []
    for item in a:
        if item > 0:
            positives.append(item)
    positives.sort()
    if positives[0] != 1:
        return 1
    for i in range(1, len(positives)-1):
        if positives[i] != positives[i-1] + 1:
            return positives[i-1] + 1
    return positives[-1] + 1

# Tests
print(solution([3, 4, -1, 1])) # 2
print(solution([1, 2, 0])) # 3

