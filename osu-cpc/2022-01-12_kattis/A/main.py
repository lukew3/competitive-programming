s = input()
l = int(len(s)/3)
o = ''
for i in range(l):
    if s[i] == s[i+l]:
        o += s[i]
    elif s[i] == s[i+2*l]:
        o += s[i]
    else:
        o += s[i+l]
print(o)
