#You can go your own way
from sys import stdin

def main():
    inData = []
    for line in stdin:
        line = line.rstrip()
        inData.append(line)
    caseCount = inData[0]
    curCase=1
    firstIndex = curCase
    while curCase <= int(caseCount):
        size = inData[firstIndex]
        ogstr = inData[firstIndex + 1]
        newPath = newPattern(ogstr)
        print("Case #" + str(curCase) + ": " + newPath)
        curCase = curCase + 1
        firstIndex = firstIndex+2

def newPattern(ogpath):
    newpath = ogpath.replace("E", "1")
    newpath = newpath.replace("S", "0")
    newpath = newpath.replace("1", "S")
    newpath = newpath.replace("0", "E")
    return newpath

main()
