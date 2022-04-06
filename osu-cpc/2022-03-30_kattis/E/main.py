def solution(n, k):
    s = [False] * n
    for _ in range(k):
        i = 0
        while i < len(s):
            if s[i] == False:
                s[i] = True
                i = len(s)
            else:
                s[i] = False
            i += 1
    if s[-1] == True:
        return "ON"
    else:
        return "OFF"

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    print(f"Case #{i+1}: {solution(n, k)}")
