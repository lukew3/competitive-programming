import sys

x = 0
y = 0
a = 0
for line in sys.stdin:
    s = line.split()
    if s[0] == 'forward':
        x += int(s[1])
        y += a * int(s[1])
    elif s[0] == 'down':
        a += int(s[1])
    elif s[0] == 'up':
        a -= int(s[1])
print(x*y)
