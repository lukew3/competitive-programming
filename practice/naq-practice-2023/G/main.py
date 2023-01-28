c = input()
s = input()
key = s
lastm = ''
message = ''
for i in range(len(c)):
    lastmc = ord(c[i]) - (ord(key[i]) - 65)
    if lastmc < 65:
        lastmc += 26
    elif lastmc > 91:
        lastmc -= 26
    lastm = chr(lastmc)
    key += lastm
print(key[len(s):])
