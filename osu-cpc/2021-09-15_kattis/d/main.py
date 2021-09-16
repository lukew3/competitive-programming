import sys
def countsub(sub, full):
    c = 0
    for i in range(0, len(full)-len(sub)+1):
        if full[i:i+len(sub)] == sub:
            c += 1
    return c

for line in sys.stdin:
    if line.strip() == '0':
        break
    s, l = line.split()
    a = countsub(s, l)
    b = 0
    c = 0
    prevt = []
    for i in range(0, len(s)):
        t = s[:i] + s[i+1:]
        if t not in prevt:
            b+=countsub(t, l)
        prevt.append(t)
    o = ['A', 'G', 'C', 'T']
    prevk = []
    for i in range(0, len(s)+1):
        for j in range(0, len(o)):
            k = list(s)
            k.insert(i, o[j])
            t = ''.join(k)
            if t not in prevk:
                c += countsub(t, l)
            prevk.append(t)
    print(a,b,c)

