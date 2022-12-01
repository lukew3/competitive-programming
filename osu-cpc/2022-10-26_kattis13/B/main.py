n = int(input())
a = []
inc = True
dec = True
last = input()
for i in range(n-1):
    line = input()
    if inc:
        inc = line > last
    if dec:
        dec = line < last
    last = line

if inc:
    print("INCREASING")
elif dec:
    print("DECREASING")
else:
    print("NEITHER")
