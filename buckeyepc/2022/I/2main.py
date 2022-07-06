n = int(input())
s = input()
v = 0
for i in range(n):
    v = (v * 10 + int(s[i])) % 11
print(v)
