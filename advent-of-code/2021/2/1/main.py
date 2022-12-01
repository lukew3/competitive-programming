import sys

x = 0
y = 0
for line in sys.stdin:
    s = line.split()
    if s[0] == 'forward':
        x += int(s[1])
    elif s[0] == 'down':
        y += int(s[1])
    elif s[0] == 'up':
        y -= int(s[1])
print(x*y)
