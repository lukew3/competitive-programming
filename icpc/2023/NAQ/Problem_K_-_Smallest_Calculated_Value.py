a, b, c = map(int, input().split())
ops = ['+', '-', '*', '/']
minn = a*b*c
for op in ops:
    if op == '/' and a % b != 0:
        continue
    ab = eval(str(a) + op + str(b))
    for op2 in ops:
        if op2 == '/' and ab % c != 0:
            continue
        abc = eval(str(ab) + op2 + str(c))
        if abc >= 0:
            minn = min(minn, abc)
        #print(op, op2, abc)
print(int(minn))