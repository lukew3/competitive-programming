import sys
for line in sys.stdin:
    out = str(round(eval(line), 2))
    try:
        if out[-3] == '.':
            print(out)
        elif out[-2] == '.':
            print(out + "0")
        else:
            print(out + ".00")
    except Exception:
        print(out + ".00")
