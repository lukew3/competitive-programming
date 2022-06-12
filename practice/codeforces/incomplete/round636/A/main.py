def findx(n):
    solved = False
    k=1
    divisor = 1
    while solved == False:
        k+=1
        divisor += (2 ** (k-1))
        if n%divisor == 0:
            solved = True
    return int(n/divisor)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(findx(n))
