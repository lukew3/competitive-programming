import sys

def findCenter(a, b):
    for x in range(-6, 7):
        for y in range(-6, 7):
            print(str(x) + " " + str(y))
            s = str(input())
            if s == "CENTER":
                break
            sys.stdout.flush()
        if s == "CENTER":
            break

if __name__ == "__main__":
    t, a, b = map(int, input().split())
    for _ in range(t):
        findCenter(a,b)
