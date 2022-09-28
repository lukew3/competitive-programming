def solve():
    s = input()
    q = int(input())
    summ = 0
    for _ in range(q):
        l, r = map(int, input().split())
        if (l-r)%2 != 0:
            # impossible if even # of digits
            continue

        left = sorted(s[l-1:int((l+r)/2)])
        right = sorted(s[int((l+r)/2-1): r])

        if left == right:
            # remove middle digit
            summ += 1
            continue

        offset = 0
        for i in range(len(left)):
            if left[i-offset] != right[i]:
                if left[i] == right[i+1]:
                    offset = -1
                elif left[i+1] == right:
                    offset = 1
                else:
                    break

        print(left)
        print(right)
        print(sub)
        
    return summ

t = int(input())
for case_num in range(t):
    print(f"Case #{case_num+1}: {solve()}")
