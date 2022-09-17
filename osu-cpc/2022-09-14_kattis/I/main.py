import sys

s = {}
for line in sys.stdin:
    l = line.split()
    if l[0] == 'define':
        s[l[2]] = l[1]
    elif l[0] == 'eval':
        if l[1] not in s or l[3] not in s:
            print('undefined')
            continue
        if l[2] == '<':
            print(s[l[1]] < s[l[3]])
        elif l[2] == '=':
            print(s[l[1]] == s[l[3]])
        elif l[2] == '>':
            print(s[l[1]] > s[l[3]])

