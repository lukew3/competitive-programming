import sys

tail_set = set([(0,0)])
hx = 0
hy = 0
tx = 0
ty = 0
for line in sys.stdin:
    cmd = line.split()
    for i in range(int(cmd[1])):
        if cmd[0] == 'R':
            hx += 1
            if hx-tx == 2:
                tx += 1
                if hy-ty == 1:
                    ty += 1
                elif hy-ty == -1:
                    ty -= 1
        elif cmd[0] == 'L':
            hx -= 1
            if hx-tx == -2:
                tx -= 1
                if hy-ty == 1:
                    ty += 1
                elif hy-ty == -1:
                    ty -= 1
        elif cmd[0] == 'U':
            hy += 1
            if hy-ty == 2:
                ty += 1
                if hx-tx == 1:
                    tx += 1
                elif hx-tx == -1:
                    tx -= 1
        elif cmd[0] == 'D':
            hy -= 1
            if hy-ty == -2:
                ty -= 1
                if hx-tx == 1:
                    tx += 1
                elif hx-tx == -1:
                    tx -= 1
        print(tx,ty)
        tail_set.add((tx, ty))
print(len(tail_set))

