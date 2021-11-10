import sys
target = 0
curlist = []
firstline = True
secondline = True
for line in sys.stdin:
    line = line.strip()
    if line.isnumeric():
        if firstline:
            firstline = False
        else:
            if secondline:
                secondline = False
            else:
                print("")
        target = int(line)
        if len(curlist) != 0:
            curlist.sort()
            for item in curlist:
                print(item)
            curlist = []
    else:
        curlist.append(line)

