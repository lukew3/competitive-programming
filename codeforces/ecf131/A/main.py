def main():
    t = int(input())
    for _ in range(t):
        s = 0
        for i in input().split():
            s += int(i)
        for i in input().split():
            s += int(i)
        if s == 0:
            print(0)
        elif s == 4:
            print(2)
        else:
            print(1)

main()
