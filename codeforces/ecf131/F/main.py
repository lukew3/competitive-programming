import bisect
points = []

def beautiful(d):
    b = 0
    for i in range(len(points)-2):
        for j in range(i+1, len(points)-1):
            for k in range(j+1, len(points)):
                b += int(points[k] - points[i] <= d)
    return b

def main():
    q, d = map(int, input().split())
    a = [int(i) for i in input().split()]
    for op in a:
        if op in points:
            points.remove(op)
        else:
            bisect.insort(points, op)
        print(beautiful(d))

main()
