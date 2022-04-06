n = int(input())
s = []
for _ in range(n):
    c = input()
    if c == "enter":
        s.append(s[-1])
    elif c == "swap":
        t = s[-1]
        s[-1] = s[-2]
        s[-2] = t
    elif c == "+":
        s[-2] += s[-1]
        s.pop()
    elif c == "-":
        # which num is being subtracted from which?
        s[-2] -= s[-1]
        #s[-2] = s[-1] - s[-2]
        s.pop()
    elif c == "*":
        s[-2] *= s[-1]
        s.pop()
    elif c == "/":
        s[-2] /= s[-1]
        #s[-2] = s[-1] / s[-2]
        s.pop()
    else:
        if len(s) == 0:
            s.append(int(c))
        else:
            s[-1] = int(c)
print(int(s[-1]))

