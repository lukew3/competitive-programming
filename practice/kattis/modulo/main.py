import sys
r = []
for line in sys.stdin:
    r.append(int(line.strip())%42)
print(len(set(r)))

