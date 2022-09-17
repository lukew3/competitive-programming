def solve():
        n, k = map(int, input().split())
        s = [int(i) for i in input().split()]
        if len(s) > k*2:
            return "NO"
        # Return NO if a style appears more than twice
        count_dict = {}
        for item in s:
            if item in count_dict:
                count_dict[item] += 1
                if count_dict[item] == 3:
                    return "NO"
            else:
                count_dict[item] = 1
        return "YES"

if __name__ == '__main__':
    t = int(input())
    for case_num in range(t):
        print(f"Case #{case_num+1}: {solve()}")
