t = int(input())

def solve(n, s):
    front=True
    score = 0
    w = 0
    for j in range(n):
        if front:
            if s[j] == '0':
                w += 1
            elif s[j] == '1':
                score = int((w*(w+1))/2)
                front=False
                w = 0
        else:
            if s[j] == '0':
                w += 1
            elif s[j] == '1':
                h = int(w/2)
                score += h*(h+1)
                if w%2 !=0:
                    score += h+1
                w = 0
    score += int((w*(w+1))/2)
    return str(score)

for i in range(t):
    n = int(input())
    s = input()
    print(f"Case #{i+1}: " + solve(n, s)) 
