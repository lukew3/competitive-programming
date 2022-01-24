def findLower(n):
    a = int(n[0])-1
    digFound = False
    while not digFound:
        if str(a) in n:
            a-=1
            if str(a) == 0:
                return False
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
        if str(a) in n:
            a+=1
            if str(a) == 10:
                return False
        else:
            digFound = True
    smallest = 0
    while str(smallest) in n:
        smallest+=1
        if smallest == 10:
            return False
    return f"{a}{str(smallest)*(len(n)-1)}"


def main():
    n = input()
    # find closest front place
    l = findLower(n)
    u = findUpper(n)
    if not l and not u:
        print("Impossible")
    elif l and not u:
        print(l)
    elif u and not l:
        print(u)
    elif int(u)-int(n) > int(n)-int(l):
        print(l)
    elif int(u)-int(n) < int(n)-int(l):
        print(u)
    else:
        print(l, u)


main()
