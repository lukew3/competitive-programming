def main():
    s = input().split()
    x = s[0]
    y = s[2]
    z = s[4]

    if len(x) != 1 and len(y) != 1:
        for i in range(1, len(x)):
            x1 = x[:i]
            x2 = x[i:]
            for j in range(1, len(y)):
                y1 = y[:j]
                y2 = y[j:]
                left1 = y1+x2+" "+s[1]+" "+x1+y2
                if eval(left1) == int(z):
                    return left1 + " = " + z
    if len(x) != 1 and len(z) != 1:
        for i in range(1, len(x)):
            x1 = x[:i]
            x2 = x[i:]
            for j in range(1, len(z)):
                z1 = z[:j]
                z2 = z[j:]
                left2 = z1+x2+" "+s[1]+" "+y
                right2 = x1+z2
                if eval(left2) == eval(right2):
                    return left2 + " = " + right2
    if len(y) != 1 and len(z) != 1:
        for i in range(1, len(y)):
            y1 = y[:i]
            y2 = y[i:]
            for j in range(1, len(z)):
                z1 = z[:j]
                z2 = z[j:]
                left3 = x+" "+s[1]+" "+z1+y2
                right3 = y1+z2
                if eval(left3) == eval(right3):
                    return left3 + " = " + right3
                
print(main())