nums = [10, 15, 4, 6]
k = 17

def solution(nums, k):
    search_list = []
    for item in nums:
        if item in search_list:
            return True
        search_list.append(k-item)
    return False

print(solution(nums, k))
