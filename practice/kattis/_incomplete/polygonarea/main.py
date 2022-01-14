def solve(n):
    a = 0
    points = []
    for _ in range(n):
        points.append([int(i) for i in input().split()])
    print(points)
    print(f'{dir} {round(a, 1)}')

def main():
    n = int(input())
    solve(n)
main()
