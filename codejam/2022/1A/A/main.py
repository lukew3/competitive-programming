def solve(s):
    out = ""
    dupLen = 0
    # if next is greater, double current
    for i in range(len(s)-1):
        out += s[i]
        if s[i+1] == s[i]:
            dupLen+=1
        elif s[i+1] > s[i]:
            out += s[i]
            if dupLen > 0:
                out += dupLen * s[i]
                dupLen = 0
    out += s[-1]
    return out

t = int(input())
for i in range(t):
    print(f"Case #{i+1}: {solve(input())}")

#BBA
