import sys

s = 0
for line in sys.stdin:
    s1 = set(line[:len(line)//2])
    s2 = set(line[len(line)//2:])
    z = s1.intersection(s2).pop()
    if z.isupper():
        s += ord(z) - 38
    else:
        s += ord(z) - 96
print(s)
