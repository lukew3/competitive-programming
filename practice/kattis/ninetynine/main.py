def turn():
    n = int(input())
    if n == 99:
        return
    d = 99 - n
    m = d % 3
    if m == 0:
        x = n + 2
    else:
        x = n + m
    print(x)
    if x == 99:
        return
    turn()

def main():
    print(1)
    turn()

main()
