def solve(s):
    i = 0
    s = [char for char in s]
    while i < len(s):
        s2 = s
        s2.insert(i, s[i]) 
        if "".join(s2) > "".join(s):
            s = s2
            i+=1
        i+=1
    return "".join(s)

t = int(input())
for i in range(t):
    print(f"Case #{i+1}: {solve(input())}")

#BBA
