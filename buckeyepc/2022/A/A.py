w, h = map(int, input().split())
s = input()
for i in range(h):
    print(s[i*w:(i+1)*w])
