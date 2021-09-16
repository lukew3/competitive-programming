def getNameSolution(strings):
    masterString = ""
    masterList = []
    frontList = []
    middleList = []
    backList = []
    for item in strings:
        loc = item.find('*')
        if loc == 0:
            frontList.append(item)
        elif loc > 0 and loc < (item.length()-1):
            middleList.append(item)
        else:
            backList.append(item)

    if backList.length() == 0 and frontList.length() == 0:
        return "*"
    elif :

    print(frontList)
    print(middleList)
    print(backList)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        strings = []
        for _ in range(n):
            strings.append(str(input()))
        getNameSolution(strings)
        print(strings)
