def solve():
    s = input()
    q = int(input())
    summ = 0
    for _ in range(q):
        l, r = map(int, input().split())
        if (l-r)%2 != 0:
            # impossible if even # of digits
            continue

        left = s[l-1:int((l+r)/2)]
        l_ord = 0
        for char in left:
            l_ord += ord(char)

        right = s[int((l+r)/2-1): r]
        r_ord = 0
        for char in right:
            r_ord += ord(char)

        if l_ord == r_ord:
            # remove middle digit
            summ += 1
            continue
        elif l_ord > r_ord:
            r_ord -= 
            for char in left:
                if l_ord - ord(char) == r_ord:
                    summ += 1
                    break
        else:
            for char in right:
                if r_ord - ord(char) == l_ord:
                    summ += 1
                    break
        print(left)
        print(right)
        
    return summ

t = int(input())
for case_num in range(t):
    print(f"Case #{case_num+1}: {solve()}")
