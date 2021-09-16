from collections import Counter

def calcCuts(diners, slicesList, cutsCount, size):

    dups = [k for k,v in Counter(slicesList).items() if v>1]
    if diners == 2 and dups != []:
        return 0
    elif diners == 3 and dups != [] and any(y > (x for x in dups) for y in slicesList):
        return 0
    elif diners == 2:
        return 1
    elif diners ==3 and dups != [] and not any(y > (x for x in dups) for y in slicesList):
        return 1
    elif diners == 3 and dups == []:
        for y in slicesList:
            for x in slicesList:
                if (y/2) == x:
                    return 1
    else:
        return 2
    return 2

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, d = map(int, input().split())
        slices = list(map(int, input().split()))
        cuts = calcCuts(d, slices, 0, -1)
        print("Case #" + str(i+1) + ": " + str(cuts))
