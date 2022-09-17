def solve(case_num):
    r, c = map(int, input().split())
    if r != 1 and c != 1:
        print(f"Case #{case_num}: Possible")
        for _ in range(r):
            input() # clear input
            print("^" * c)
    else:
        for i in range(r):
            line = input()
            if '^' in line:
                print(f"Case #{case_num}: Impossible")
                for _ in range(r-i-1):
                    input()
                return
        print(f"Case #{case_num}: Possible")
        for _ in range(r):
            print('.' * c)

t = int(input())
for case in range(t):
    solve(case+1)
