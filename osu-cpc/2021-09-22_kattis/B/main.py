import sys
count = 1
target = 0
curlist = []
for line in sys.stdin:
    if count < target:
        curlist.append(line.strip())
        count += 1
    else:
        if len(curlist) != 0:
            curlist.sort()
            for item in curlist:
                print(item)
            print("")
        target = int(line)
        count = 0
        curlist = []




