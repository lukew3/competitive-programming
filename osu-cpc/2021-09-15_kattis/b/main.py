n = int(input())
for _ in range(n):
    s = input()
    if "Simon says" in s:
        print(s[11:])
