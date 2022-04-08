input()
s = input()
o = 0
e = 0
for i in range(len(s)):
    if i%2 == 0:
        o += int(s[i])
    else:
        e += int(s[i])
print((o-e)%11)

