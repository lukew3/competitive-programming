import sys

s = 0
count = 0
myset = {}
for line in sys.stdin:
    count += 1
    if count == 1:
        myset = set(line[:-1])
    else:
        myset = myset.intersection(set(line[:-1]))
        if count == 3:
            o = myset.pop()
            myset = {}
            if o.isupper():
                s += ord(o) - 38
            else:
                s += ord(o) - 96
            count = 0
print(s)
