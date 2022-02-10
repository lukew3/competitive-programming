def findLower(n):
    a = int(n[0])-1
    digFound = False
    while not digFound:
        if a == -1:
            a = ""
            break
        if str(a) in n:
            a-=1
        else:
            digFound = True
    greatest = 9
    while str(greatest) in n:
        greatest-=1
        if greatest == -1:
            return False
    return f"{a}{str(greatest)*(len(n)-1)}"

def findUpper(n):
    a = int(n[0])+1
    digFound = False
    while not digFound:
        # catch herr
        if a == 10:
            if str(1) in n:
                return False
            else:
                digFound = True
        if str(a) in n:
            a+=1
        else:
            digFound = True
    smallest = 0
    while str(smallest) in n:
        smallest+=1
        if smallest == 10:
            return False
    return f"{a}{str(smallest)*(len(n)-1)}"


def main():
    n = str(int(input()))
    # find closest front place
    l = findLower(n)
    u = findUpper(n)
    if l and int(l) == 0:
        l = False
    if u and int(u) == 0:
        u = False
    if not l and not u:
        print("Impossible")
    elif l and not u:
        print(int(l))
    elif u and not l:
        print(int(u))
    elif int(u)-int(n) > int(n)-int(l):
        print(int(l))
    elif int(u)-int(n) < int(n)-int(l):
        print(int(u))
    else:
        print(int(l), int(u))

main()
