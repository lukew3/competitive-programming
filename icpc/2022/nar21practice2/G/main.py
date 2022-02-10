def main():
    n = int(input())
    xmin, ymin, xmax, ymax = map(int, input().split())
    for i in range(n-1):
        x1, y1, x2, y2 = map(int, input().split())
        if x1 < xmin:
            xmin = x1
        if y1 < ymin:
            ymin = y1
        if x2 > xmax:
            xmax = x2
        if y2 > ymax:
            ymax = y2
    print(xmin, xmax)
    print(ymin, ymax)
    print(xmax-xmin)
    print(ymax-ymin)
    a = (ymax-ymin) * (xmax-xmin)
    print(a)

main()
