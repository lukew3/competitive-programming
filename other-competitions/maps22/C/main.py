def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    q = int(input())
    solved = False
    i = 0
    while not solved:
        while a[i] != i + 1:
            x = a[a[i] - 1]
            a[a[i] - 1] = a[i]
            a[i] = x
            if x == q:
                solved = True
                break
    return a

print(main())

