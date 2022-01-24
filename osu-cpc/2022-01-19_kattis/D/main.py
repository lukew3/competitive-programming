def checkRepeat(sub):
    c = 0
    for char in sub:
        if char == sub[0] or char == sub[-1]:
            c += 1
        if c > 2:
            return False
    return True

s = input()
c = 0
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        u = s[i:j+1]
        if u[0] != u[-1] and checkRepeat(u):
            c+=1
print(c)
