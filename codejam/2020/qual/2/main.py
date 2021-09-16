def main():
    numCases = int(input())
    for i in range(numCases):
        s = [char for char in str(input())]

        #group numbers based on value
        subS = ""
        groupedList = []
        for j in range(len(s)):
            if j == 0:
                subS = str(s[j])
            elif int(s[j]) == int(s[j-1]):
                subS = subS+str(s[j])
            else:
                groupedList.append(subS)
                subS = str(s[j])
        groupedList.append(subS)

        #add parenthesis for values
        fullString = ""
        for k in range(len(groupedList)):
            val = int(str(groupedList[k])[:1])
            partString = ""
            for l in range(val):
                partString += "("
            partString += str(groupedList[k])
            for l in range(val):
                partString += ")"
            fullString += partString

        #Delete extra parenthesis from final result
        complexS = [char for char in str(fullString)]
        complete = False

        while complete == False:
            lastchar = ""
            editsMade = False
            for j in range(int(len(complexS))):
                char = complexS[j]
                if ( lastchar == "(" and char == ")" ) or ( lastchar == ")" and char == "(" ):
                    del complexS[j]
                    del complexS[j-1]
                    lastchar = ""
                    editsMade = True
                    break
                else:
                    lastchar = char
            if editsMade == False:
                complete = True
        simpleString = ''.join(complexS)
        print("Case #" + str(i+1) + ": " + simpleString)

main()
