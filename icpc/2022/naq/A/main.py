def isAlien(a, b):
    digits = [False] * 10
    for char in a:
        digits[int(char)] = True



def main():
    n = int(input())
    i = 1
    solved = False
    while not solved:
        if isAlien(n, n-i):
            solved = True
            isAlien(n, n+i)
        i+=1

main()
