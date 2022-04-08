input()
s = input()
v = 0
for i in range(len(s)):
    v = (v * 10 + int(s[i])) % 11
print(v)

