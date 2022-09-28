def solve():
    n = input() #len of s
    s = [int(i) for i in input().split()]
    q = int(input())
    summ = 0
    for _ in range(q):
        a, b, c = map(int, input().split())
        if a == 1:
            s[b] = c
        elif a == 2:
            digsum = 0
            for item in s[b-1:c]:
                digsum += item
            print(digsum)
        
    return summ

t = int(input())
for case_num in range(t):
    print(f"Case #{case_num+1}: {solve()}")
