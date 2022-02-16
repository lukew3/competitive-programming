def calcBeauty(sub):
    myDict = {}
    for item in sub:
        if item not in myDict:
            myDict[item] = 0
        else:
            myDict[item] += 1
    max = 0
    min = 500 
    for char in myDict:
        if myDict[char] > max:
            max = myDict[char]
        if myDict[char] < min:
            min = myDict[char]
    return max-min

def main(s):
    sumBeauty = 0
    for i in range(len(s)):
        for j in range(len(s)+1):
            sub = s[i:j]
            if len(sub) > 0:
                sumBeauty += calcBeauty(sub)
    print(sumBeauty)
            
            
s = input()
main(s)
