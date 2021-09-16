def findDigitString(u2, tests):
    key = []
    """
    for j in range(10**4):
        if tests[j][0] == 1:
            key.append([1, tests[j][1]])
            break
    for k in range(10**4):
        if (tests[k][0] == 2) and (key[0][1] != tests[k][1]):
            key.append([2, tests[k][1]])
            break
    """
    returnString = ""
    for j in range(10):
        for k in range((100)):
            print(k)
            if tests[k][0] == j+1 and (str(key[0][1]) in returnString) == False:
                key.append([j+1, tests[k][1]])
                returnString+=str(tests[k][1])
                break

    #for l in range(len(key)):
    #    returnString+=str(key[l][1])
    print(returnString)
    return returnString




if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        u = int(input())
        inputList = []
        for i in range(10**4):
            inputLine = str(input()).split()
            inputList.append([int(inputLine[0]), str(inputLine[1])])
        #print(inputList)
        findDigitString(u, inputList)
