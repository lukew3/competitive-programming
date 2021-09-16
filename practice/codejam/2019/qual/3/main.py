from sys import stdin
from math import gcd

def main():
    inData = []
    megaList = []
    for line in stdin:
        line = line.rstrip()
        inData.append(line)
    t = int(inData[0])
    case=1
    firstIndex = case
    while case <= t:
        line1 = inData[firstIndex].split()
        n = int(line1[0])
        l = int(line1[1])
        codemsg = inData[firstIndex + 1].split()
        rawMessage = decryptMessage(n, codemsg, l)
        print("Case #" + str(case) + ": " + rawMessage)
        case = case + 1
        firstIndex = firstIndex + 2

def decryptMessage(n, ogArray, len):
    lastNum = 1
    encryptedList = []
    for i in range(0, len):
        num = int(ogArray[i])
        value = gcd(lastNum, num)
        if i == 1:
            firstValue = lastNum/value
            encryptedList[0] = int(firstValue)
        encryptedList.append(value)
        if i == len-1:
            finalValue = num/value
            encryptedList.append(int(finalValue))
        lastNum = num
    orderedList = sorted(encryptedList)
    orderedList = list(dict.fromkeys(orderedList))
    key = {orderedList[i]: chr(i+65) for i in range(26)}
    rawMessage = ''.join([key[x] for x in encryptedList])
    return rawMessage


main()
