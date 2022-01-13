import sys
def sumDigits(n):
    nstr = str(n)
    digSum = 0
    for item in nstr:
        digSum += int(item)
    return digSum

def main():
    for line in sys.stdin:
        N = int(line)
        if (N == 0):
            return
        s = sumDigits(N)
        p = 11
        while (sumDigits(N * p) != s):
            p+=1
        print(p)

main()
